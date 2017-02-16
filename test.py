import praw

reddit = praw.Reddit('Fa15Bot')

subreddit = reddit.subreddit("Fa15Memes")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")