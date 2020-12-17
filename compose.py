from datetime import datetime

#takes a row from the miiverse.db, and (currently) prints how that data would be translated into the text of a tweet 
def create_tweet_text(p):
    date = datetime.fromtimestamp(int(p[4]))
    #I replace the japanese word "コミュニティ" with "Community" for a couple reasons:
    # - as far as I'm aware, the translation is direct and unambigious, meaning nothing of cultural value is lost
    # - it makes the tweet look more gramatically correct
    return "Posted by " + p[3] + " on " + get_date(date) + " in the " + p[1].replace("コミュニティ", "Community")

#takes a datetime object, returns a string in this format: MM/DD/YYYY
#maybe ill fix it to do [Month] [Day][Suffix], [Year], but that might be wordy for a tweet.
def get_date(d):
    return str(d.month) + "/" + str(d.day) + "/" + str(d.year)