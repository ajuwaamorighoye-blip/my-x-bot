import tweepy
import os
import time

# Check environment variables
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

print("Starting bot...")
print("Environment variables loaded:")
print("API_KEY:", API_KEY is not None)
print("API_SECRET:", API_SECRET is not None)
print("ACCESS_TOKEN:", ACCESS_TOKEN is not None)
print("ACCESS_SECRET:", ACCESS_SECRET is not None)

# Authenticate with X
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
import tweepy
import time

api = tweepy.API(auth)

print("Bot authenticated successfully")

# Keep the bot alive
while True:
    try:
        api.update_status("Hello X! I am a bot 🤖")
        print("Tweet sent successfully")
        time.sleep(600)  # wait 10 minutes
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(60)  # wait 1 minute before retrying
print("Error sending tweet:", e)
time.sleep(60)
