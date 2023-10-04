import praw
import datetime
import csv 
import os
import pandas as pd

reddit = praw.Reddit (client_id = '-ezNf0eeEepLXZnIzrzHCQ', client_secret = 'JTA_we-DO6yTNrx8cIIdtSxDyayi-g', username = 'NLP_analysis', password = 'NLPproject@2023', user_agent = 'NLP')

subreddit = reddit.subreddit('wallstreetbets')
start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 1, 2)

with open('reddit_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Comment", "Reply"])
    for submission in subreddit.search("tesla", sort='hot',limit=1000):
        if start_date <= datetime.date.fromtimestamp(submission.created_utc) <= end_date:
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                for reply in comment.replies:
                    writer.writerow([submission.title, comment.body, reply.body])
    



