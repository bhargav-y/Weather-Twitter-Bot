import requests
import datetime
import tweepy
from Keys import *

url = "https://api.darksky.net/forecast/26328500523b4ae9be06626bf27b7d60/42.1103, -88.0342"
data = requests.get(url).json()

high_temp = data['daily']['data'][0]['temperatureMax']
date = data['daily']['data'][0]['time']

date = str(datetime.datetime.fromtimestamp(date))

message = "High Temp is " + str(high_temp) + " for today, " + str(date) + "."

account = tweepy.OAuthHandler(consumer_key, consumer_secret)
account.set_access_token(access_token, access_secret)

bot = tweepy.API(account)
bot.update_status(message)
