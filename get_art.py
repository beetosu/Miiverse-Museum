import csv, sqlite3
from datetime import datetime

#get the needed text for the tweet
#im probably gonna delegate the actual retreval of the image to another function
def access_db():
    conn = sqlite3.connect('miiverse.db')
    cur = conn.cursor()

    gallery = cur.execute("SELECT * FROM Posts ORDER BY RANDOM() LIMIT 10")
    for post in gallery:
        date = datetime.fromtimestamp(int(post[4]))
        print("Posted by ", post[3], " on ", get_date(date), " in the ", post[1], ": ", post[2], sep="")

    conn.close()

#datetime object->MM/DD/YYYY
#maybe ill fix it to do [Month] [Day][Suffix], [Year], but that might be wordy for a tweet.
def get_date(d):
    return str(d.month) + "/" + str(d.day) + "/" + str(d.year)

#access_db()