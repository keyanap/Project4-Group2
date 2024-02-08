# Tweepy script to fetch 2024 US Election from the Twitter 2.0 API

import tweepy
import json
from pathlib import Path
import csv
from datetime import datetime, timedelta

# Load the Twitter API keys from the environment variables

api_key = "2A9uuYhWvAzbCjL8RXsNuI1wu"
api_secret = "aqmMLtHWzr7DiriQXTrz8oBH3j8uE7EUK3nXCoqpi5TxrA05GV"
access_token = "18021882-vJ9zYrysYMOmiXKRVfdGojtWW2C2KcjA9g1fyoiS7"
access_token_secret = "IXXB964K7AMOQ2zjou1mNdrNrPofhifmbDnvViEF9Tb9h"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAP2UsAEAAAAA8BMgvbd2dKFOPs%2BkKPVA8tAg6ZA%3DXpdudtUGizA7iBlirEdY75Av8Lsc7GywU1RqGNFCKHmW4epONc"

# Authenticate to the Twitter API
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)


# Initialize Tweepy Client
client = tweepy.Client(bearer_token)

# Read keywords from a file
with open('keywords.txt', 'r') as file:
    keywords = [line.strip() for line in file if line.strip()]

# Build the query
query = " OR ".join(keywords) + " -is:retweet"
tweet_fields = ['created_at', 'geo']

# Search for tweets
tweets = client.search_recent_tweets(query=query, max_results=50, tweet_fields=tweet_fields)

# Filter for tweets with geo-data and create a DataFrame
data = []
for tweet in tweets.data:
    if tweet.geo:
        data.append({
            "text": tweet.text,
            "date": tweet.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "location": tweet.geo['place_id']
        })

df = pd.DataFrame(data)

# Perform your EDA here on the DataFrame 'df'
# For example, you can print the first few rows:
print(df.head())
