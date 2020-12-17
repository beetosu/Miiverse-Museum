import database, compose
import sqlite3

def main():
    conn = sqlite3.connect('miiverse-small.db')
    cur = conn.cursor()
    art = database.get_posts(cur)
    for post in art:
        compose.create_tweet_text(post)
    conn.close()

if __name__ == "__main__":
    main()