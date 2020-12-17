import database, compose, drawing, secrets
import sqlite3, time, tweepy
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

    #for every post, get the needed data, format it into a tweet,
    #update the database to reflect the posting, and then wait 4 hours
    while len(posts) > 0:
        start = time.time()
        post = posts.pop(0)
        print(post)
        body = compose.create_tweet_text(post)
        postedDrawing = drawing.get_drawing(post[2])
        postedDrawing.save("drawing.png")
        api.update_with_media("drawing.png", status=body)
        cur.execute("UPDATE Posts SET Posted=1 WHERE Id='"+post[0]+"'")
        conn.commit()
        end = time.time()
        time.sleep(14400 - (start - end))
    conn.close()

if __name__ == "__main__":
    main()