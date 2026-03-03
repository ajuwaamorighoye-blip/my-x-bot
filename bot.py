import tweepy
import os
import time

print("Starting bot...")

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

print("Environment variables loaded:", API_KEY is not None, API_SECRET is not None)

try:
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
print("Authentication successful")
except Exception as e:
print("Authentication failed:", e)
raise e

while True:
try:
api.update_status("Hello X! I am a bot 🤖")
print("Tweet sent successfully")
time.sleep(600)
except Exception as e:
pri
