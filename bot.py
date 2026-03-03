import tweepy
import os
import time

# Get API keys from environment variables
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# Authenticate
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

print("Bot is running...")

# Keep the bot alive
while True:
try:
api.update_status("Hello X! I am a bot 🤖")
print("Tweet sent successfully")
time.sleep(600) # wait 10 minutes before next tweet
except Exception as e:
print("Error:", e)
time.sleep(60) # wait 1 minute before retry
