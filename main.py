import database, compose, drawing, secrets
import sqlite3, time, tweepy
from datetime import datetime, timedelta
from PIL import Image

#this is what is called, and where the main tweet loop is
def main():
    #get the needed posts from the database
    conn = sqlite3.connect('miiverse-small.db')
    cur = conn.cursor()
    posts = database.get_posts(cur)

    #load the twitter api
    auth = tweepy.OAuthHandler(secrets.API_KEY, secrets.API_SECRET_KEY)
    auth.set_access_token(secrets.ACCESS_TOKEN, secrets.ACCESS_SECRET)
    api = tweepy.API(auth)

    #wait for the first interval (12a, 4a, 8a, etc. in EST)
    currentHour = datetime.now().replace(second=0, microsecond=0, minute=0) - timedelta(hours=5)
    currentHour += timedelta(hours=1)
    while currentHour.hour % 4 != 0:
        currentHour += timedelta(hours=1)
    currentHour += timedelta(hours=5)
    time.sleep((currentHour - datetime.now()).total_seconds())

    #for every post, get the needed data, format it into a tweet,
    #update the database to reflect the posting, and then wait 4 hours
    while len(posts) > 0:
        start = time.time()
        post = posts.pop(0)
        body = compose.create_tweet_text(post)
        postedDrawing = drawing.get_drawing(post[2])
        postedDrawing.save("drawing.png")
        api.update_with_media("drawing.png", status=body)
        cur.execute("UPDATE Posts SET Posted=1 WHERE Id='"+post[0]+"'")
        conn.commit()
        end = time.time()
        durationTime = end - start
        time.sleep(14400 - durationTime)
    conn.close()

if __name__ == "__main__":
    main()