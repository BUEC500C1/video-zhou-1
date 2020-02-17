# !/usr/bin/env python3
'''
Copyright @2020 Zhou Shen
HW 4 - #1
'''

import tweepy
import re
from textToImg import textToImg

def tweepy_info(twitterUsr):
  ##
  ## Delete all for below info!!! !!! !!!!
  ## Put your own twitter API info here
  ##
  consumer_key = ''
  consumer_secret = ''
  access_token = ''
  access_token_secret = ''
  
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
  auth.set_access_token(access_token, access_token_secret)   
  api = tweepy.API(auth)

  search_results = api.user_timeline(twitterUsr)

  twitterNum = 0
  highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
  for tweet in search_results:
    gap = '\n'
    tweet_list = list(tweet.text)

    list_num = 0
    for i in range(len(tweet_list)):
      if (i % 50) == 0:
        tweet_list.insert(i,gap)
    # tweet_list.insert(55, gap)
    tweet.text = ''.join(tweet_list)
    print(tweet.text)

    # convert format of text
    text_noem = highpoints.sub('--emoji--', tweet.text)
    text_noem = text_noem.encode('utf8')

    # add 1 for number of images
    twitterNum += 1

    textToImg(text_noem, twitterUsr, twitterNum)


## test only
tweepy_info("BU_ece")
