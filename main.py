import json
import os
PATH = ["farmers-protest-tweets-2021-03-5.json"]

path = os.path.join(*PATH)

def top_tweets(tweets):
  tweets = sorted(tweets, key=lambda tweet: tweet["retweetCount"])
  return tweets[0: 10]


def main():
  tweets = [json.loads(line)
        for line in open(path, 'r', encoding='utf-8')]
  print(top_tweets(tweets))

main()
