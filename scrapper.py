import praw
import pandas as pd

# Authenticate
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='YOUR_USER_AGENT'
)

# Scrape posts from subreddit
subreddit = reddit.subreddit('stocks')
posts = []
for post in subreddit.hot(limit=100):
    posts.append([post.title, post.selftext, post.score, post.num_comments, post.created_utc])

# Save to DataFrame
df = pd.DataFrame(posts, columns=['Title', 'Body', 'Score', 'Comments', 'Timestamp'])
df.to_csv('reddit_posts.csv', index=False)
