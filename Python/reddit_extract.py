import praw

# Create your access keys in https://www.reddit.com/prefs/apps for python reddit data extraction
# Enter your client id, client secret, user agent details
reddit = praw.Reddit(
    # Client ID
    client_id="",
    # Client Secret Key
    client_secret="",
    # User Agent
    user_agent="",
    check_for_async=False
)


# Search by subreddits only
def subreddit_extraction(subreddit):
    for submission in reddit.subreddit(subreddit).hot(limit=None):
        print(submission.title)
        print("\n")
    print("The data from the given subreddit has been extracted successfully.\n")


if __name__ == "__main__":
    subreddit_extraction(subreddit_extraction())
