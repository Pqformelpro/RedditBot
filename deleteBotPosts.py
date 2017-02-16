import praw
import os

# Create the Reddit instance
reddit = praw.Reddit('Fa15Bot')

# Get the top values from our subreddit
subreddit = reddit.subreddit('Fa15Memes')

for submission in subreddit.hot():

    submission.comments.replace_more(limit=0)

    for comment in submission.comments.list():

        if not comment.author:
            continue

        if comment.author.name == "Fa15Bot":
            comment.delete()
