import csv, sqlite3
from datetime import datetime

#get a batch of drawings, along with the needed metadata
def access_db():
    '''
    the database miiverse.db has one table named "Posts"
    the following are the columns in the table, in order:
    Id: The ID of the specific row
    Community: The community a specific drawing was posted to
    Image: The archived URL of the drawing
    User: The username of the person who posted the drawing
    Timestamp: The date/time of posting, as a UNIX timestamp
    Posted: a boolean that determines if a drawing as been 
    '''
    conn = sqlite3.connect('miiverse.db')
    cur = conn.cursor()

    posts = []

    #get a random assortment of drawings that have not already been posted
    gallery = cur.execute("SELECT * FROM Posts WHERE Posted=0 ORDER BY RANDOM() LIMIT 10")
    for post in gallery:
        posts.append(list(post))
        create_tweet_text(post)
    conn.close()
    print(posts)


#takes a row from the miiverse.db, and (currently) prints how that data would be translated into the text of a tweet 
def create_tweet_text(p):
    date = datetime.fromtimestamp(int(p[4]))
    print("Posted by ", p[3], " on ", get_date(date), " in the ", p[1], sep="")

#takes a datetime object, returns a string in this format: MM/DD/YYYY
#maybe ill fix it to do [Month] [Day][Suffix], [Year], but that might be wordy for a tweet.
def get_date(d):
    return str(d.month) + "/" + str(d.day) + "/" + str(d.year)

access_db()