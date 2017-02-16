import praw
import os


REDDIT_USERNAME = "Fa15Bot"
REDDIT_PASS = "toB51aF"

# Create the Reddit instance
reddit = praw.Reddit('Fa15Bot')

# Get the top values from our subreddit
subreddit = reddit.subreddit('Fa15Memes')

for submission in subreddit.hot():
    if submission.selftext != "" and submission.is_self:
        submission.delete()
        print(submission.title + " removed")

# Have we run this code before? If not, create an empty list
if not os.path.isfile("replied_to.txt"):
    replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("replied_to.txt", "r") as file:
        replied_to = file.read()
        replied_to = replied_to.split("\n")
        replied_to = list(filter(None, replied_to))

for submission in subreddit.hot():

    if submission.id not in replied_to:
        submission.reply("Nice Post!")
        submission.upvote()
        replied_to.append(submission.id)
        print("Bot replying to submission ", submission.title)

    submission.comments.replace_more(limit=0)

    for comment in submission.comments.list():
        if comment.body.lower() == "hello bot" and comment.id not in replied_to:
            comment.reply('Hello!')
            # Store the current id into our list
            replied_to.append(comment.id)
            print("Bot replying to comment in : ", submission.title)

        try:
            if comment.author.name == "megaspinner" and comment.id not in replied_to:
                comment.reply('Hello ' + comment.author.name + "!")
                # Store the current id into our list
                replied_to.append(comment.id)
                print("Bot replying to comment in : ", submission.title)

            if comment.author.name == "Pudby" and comment.id not in replied_to:
                comment.reply('Hello ' + comment.author.name + "!")
                # Store the current id into our list
                replied_to.append(comment.id)
                print("Bot replying to comment in : ", submission.title)

        except:
            print("deleted/removed comment in " + submission.title)

# Write our updated list back to the file
with open("replied_to.txt", "w") as file:
    for replied_id in replied_to:
        file.write(replied_id + "\n")
