import json
import os
PATH = ["farmers-protest-tweets-2021-03-5.json"]

path = os.path.join(*PATH)

def top_tweets(tweets):
  tweets = sorted(tweets, key=lambda tweet: tweet["retweetCount"])
  return tweets[0: 10]

def users_with_more_tweets(tweets):
  counter = {}
  for tweet in tweets:
    username = tweet["user"]["username"]

    if username not in counter:
      counter[username] = 0

    counter[username] += 1
  
  ordered_users = dict(sorted(counter.items(), key=lambda item: item[1]))
  return list(ordered_users.keys())[0:10]

def top_10_days_with_more_tweets(tweets):
  counter = {}
  for tweet in tweets:
    day = tweet["date"][0:10]

    if day not in counter:
      counter[day] = 0

    counter[day] += 1
  
  ordered_days = dict(sorted(counter.items(), key=lambda item: item[1]))
  return list(ordered_days.keys())[0:10]

def top_10_hashtags(tweets):
  counter = {}
  for tweet in tweets:
    
    content = tweet["content"]
    words = content.split()
    hashtags = [word for word in words if word[0] == "#"]
    for hashtag in hashtags:
      if hashtag not in counter:
        counter[hashtag] = 0
      counter[hashtag] += 1
  
  ordered_hashtags = dict(sorted(counter.items(), key=lambda item: item[1]))
  return list(ordered_hashtags.keys())[0:10]

def main():
  tweets = [json.loads(line)
        for line in open(path, 'r', encoding='utf-8')]
  print(top_tweets(tweets))
  print(users_with_more_tweets(tweets))
  print(top_10_days_with_more_tweets(tweets))
  print(top_10_hashtags(tweets))

main()
