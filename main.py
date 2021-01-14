import praw
import re


def find_whole_word(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


def check_submission(sub_id):
    reddit = praw.Reddit("bot1")
    submission = reddit.submission(sub_id)
    return check_votes(submission)


def get_max(a, b, c, d):
    maximum = a
    if b.votes > maximum.votes:
        maximum = b
    if c.votes > maximum.votes:
        maximum = c
    if d.votes > maximum.votes:
        maximum = d
    list_max = []
    if a.votes == maximum.votes:
        list_max.append(a)
    if b.votes == maximum.votes:
        list_max.append(b)
    if c.votes == maximum.votes:
        list_max.append(c)
    if d.votes == maximum.votes:
        list_max.append(d)
    return list_max


def check_votes(submission):
    class Vote:
        def __init__(self, name, votes):
            self.name = name
            self.votes = votes

    esh = Vote("esh", 0)
    nta = Vote("nta", 0)
    yta = Vote("yta", 0)
    ytja = Vote("ytja", 0)
    submission.comments.replace_more(limit=None)
    # print(submission.id)
    for comment in submission.comments.list():
        if find_whole_word("esh")(str.lower(comment.body)):
            esh.votes += 1
        elif find_whole_word("nta")(str.lower(comment.body)):
            nta.votes += 1
        elif find_whole_word("yta")(str.lower(comment.body)):
            yta.votes += 1
        elif find_whole_word("ytja")(str.lower(comment.body)):
            ytja.votes += 1
    maxima = get_max(esh, nta, yta, ytja)
    if len(maxima) > 1:
        return "tie"
    else:
        return maxima[0].name
