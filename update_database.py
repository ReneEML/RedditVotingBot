import praw
from insert_postgre import insert_submission


def update_db():
    try:
        print("Connecting to Reddit...")
        reddit = praw.Reddit("bot1")
        print("Retrieving submissions...")
        subreddit = reddit.subreddit("Fictional_AITA")

        for submission in subreddit.stream.submissions(skip_existing=True):
            print(insert_submission(submission.id, int(submission.created_utc), submission.author.name))
    except(Exception, str) as error:
        print(error)

