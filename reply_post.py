import praw
import os
from random import randint

# Create the Reddit instance
reddit = praw.Reddit('Fa15Bot')

# Get the top values from our subreddit
subreddit = reddit.subreddit('Fa15Memes')

submissionReply = list()
submissionReply.append("WHAT?! SICK MEME DUDE!!")
submissionReply.append("Yo bruh nice meme you got there")
submissionReply.append("Shiet this is dope")
submissionReply.append("Well memed my friend.")
submissionReply.append("Thats what im talking 'bout")
submissionReply.append("Keep up the good work ma dude")
submissionReply.append("Sweet Jesus this is a nice meme")
submissionReply.append("ZOMG !!11! 7H15 M3M3 !S 1337")
submissionReply.append("HORY SHIET, THIS MEME IS HIGH QUALITY! WOOOOOOOOOOOOOOOOOOOOOOOW")
submissionReply.append("hehe xd")


def getRandomReply():
    x = randint(0, len(submissionReply)-1)
    return submissionReply[x]


for submission in subreddit.hot():
    if (submission.selftext != "" or submission.is_self) and submission.stickied is False:
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
        submission.reply(getRandomReply())
        submission.upvote()
        replied_to.append(submission.id)
        print("Bot replying to submission ", submission.title)

    submission.comments.replace_more(limit=0)

    for comment in submission.comments.list():
        if not comment.author:
            continue

        if comment.body.lower() == "hello bot" and comment.id not in replied_to:
            comment.reply('Hello ' + comment.author.name + '!')
            # Store the current id into our list
            replied_to.append(comment.id)
            print("Bot replying to comment in : ", submission.title)

        if comment.author.name is not "Fa15Bot" and comment.author.name is not "Blutsturm":
            continue

        if comment.id not in replied_to:
            comment.reply('Hello ' + comment.author.name + "!")
            # Store the current id into our list
            replied_to.append(comment.id)
            print("Bot replying to comment in : ", submission.title)


# Write our updated list back to the file
with open("replied_to.txt", "w") as file:
    for replied_id in replied_to:
        file.write(replied_id + "\n")
