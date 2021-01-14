from main import check_submission
import praw
from select_postgre import get_id
from update_postgre import update_submission


def db_check():
    try:
        print("Starting database check...")
        my_result = get_id()
        reddit = praw.Reddit("bot1")
        for x in my_result:
            sub_id = x[0]
            print(sub_id)
            submission = reddit.submission(sub_id)
            result = check_submission(sub_id)
            if result != "tie":
                flair_id = ""
                for k in submission.flair.choices():
                    if k["flair_text"] == str.upper(result):
                        flair_id = k["flair_template_id"]
                        print("Flair_id: " + flair_id)
                submission.flair.select(flair_id)
            print(result)
            update_submission(sub_id, result)
    except Exception as error:
        print(error)
    finally:
        return
