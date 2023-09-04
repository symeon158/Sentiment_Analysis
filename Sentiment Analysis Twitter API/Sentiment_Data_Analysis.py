import tweepy
from textblob import TextBlob
import pandas as pd
import re
import matplotlib.pyplot as plt

# Set up the Twitter API client
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Define the categories and the search query
categories = ["Excel", "Power BI", "Python"]

# Define the regular expression patterns for each category
category_patterns = {
    "Excel": r"\bexcel\b|\bexcelled\b|\bexcelerate\b|\bexcelsior\b",
    "Power BI": r"\bpowerbi\b|\bpower\sbi\b|\bpbi\b",
    "Python": r"\bpython\b|\bpy\b",
}

# Compile the regular expression patterns
compiled_patterns = {category: re.compile(pattern, re.IGNORECASE) for category, pattern in category_patterns.items()}

# Define a function to extract the category from the tweet text
def extract_category(tweet_text):
    for category, pattern in compiled_patterns.items():
        if pattern.search(tweet_text):
            return category
    return "Other"
query = " OR ".join(categories)

# Define the location and the date range
location = "USA"
start_date = "2023-01-01"
end_date = "2023-03-31"

# Retrieve the tweets
tweets = []
for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en", geocode=f"39.8333,-98.5833,2500km", since_id=start_date, until=end_date).items(1000):
    # Extract the relevant information
    user_account = tweet.user.screen_name
    user_followers = tweet.user.followers_count
    user_tweets = tweet.user.statuses_count
    user_retweets = tweet.retweet_count
    tweet_text = re.sub(r"http\S+", "", tweet.text)  # Remove URLs
    tweet_text = re.sub(r"@\S+", "", tweet_text)  # Remove mentions
    tweet_text = tweet_text.strip()  # Remove leading/trailing whitespace
    if not tweet_text.startswith("RT") and not tweet_text.startswith("@"):  # Remove retweets and mentions-only tweets
        # Classify the sentiment using TextBlob
        sentiment = TextBlob(tweet_text).sentiment.polarity
        if sentiment > 0:
            sentiment_label = "positive"
        elif sentiment < 0:
            sentiment_label = "negative"
        else:
            sentiment_label = "neutral"
        # Extract the other information
        tweet_date = tweet.created_at
        tweet_location = tweet.user.location
        tweet_hashtags = [tag["text"] for tag in tweet.entities["hashtags"]]
        # Add the information to the list of tweets
        tweets.append([user_account, user_followers, user_tweets, user_retweets, tweet_text, tweet_date, tweet_location, tweet_hashtags, sentiment_label])

# Create a DataFrame from the tweets
df = pd.DataFrame(tweets, columns=["User Account", "Followers", "Tweets", "Retweets", "Text", "Date", "Location", "Hashtags", "Sentiment"])

# Remove duplicates in the Tweet Text column
df["Text"] = df["Text"].str.lower().str.replace("[^\w\s]", "", regex=True)
df.drop_duplicates(subset=["Text"], inplace=True)

# Apply the function to the Tweet Text column to create a new column for the category
df["Category"] = df["Text"].apply(extract_category)

# Append the DataFrame to the CSV file
with open("Sentiment_Data_Analysis.csv", "a", newline = '', encoding="utf-8") as f:
    df.to_csv(f,mode="w", header=f.tell()==0, index=False)



