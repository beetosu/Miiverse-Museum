import sqlite3

#get a batch of drawings, along with the needed metadata
def get_posts(cur):
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

    posts = []

    #get a random assortment of drawings that have not already been posted
    gallery = cur.execute("SELECT * FROM Posts WHERE Posted=0 ORDER BY RANDOM() LIMIT 10")
    for post in gallery:
        #add everything to our list, except for "Posted", which is only needed for the sake of line 22
        posts.append(list(post)[:5])
    return posts
