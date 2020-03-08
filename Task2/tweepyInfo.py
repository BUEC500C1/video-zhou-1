# !/usr/bin/env python3
'''
Copyright @2020 Zhou Shen
HW 4 - #1
'''

import os
import tweepy
import re
import configparser
import json
import pytest  # in case reading API key fails

from textToImg import textToImg

def get_oldJson(twitterUsr):
  # read Json file one by one
  with open('jsonFolder/' + twitterUsr +'.json') as json_data:
    # save json data in a dictionary
    data_dict = json.load(json_data)
    highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')

    num = 0
    for line in data_dict:
      # convert format of text
      line_noem = highpoints.sub('--emoji--', line)
      line_noem = line_noem.encode('utf8')
      # print(line_noem)
      textToImg(line_noem, twitterUsr, num)
      num += 1


def tweepy_info(twitterUsr):
  config = configparser.ConfigParser()
  # Here for testing keys exist or not
  try:
    f = open('keys')
    # Do something with the file
  except IOError:
    print("File not accessible")
  finally:
    print('keys file exists')
    f.close()

  # check for whether keys file is empty or not first
  if (os.stat('keys').st_size <= 0):
    print('No content in the key file')
    # call function for saved json file
    get_oldJson(twitterUsr)
    return

  # path here is keys
  try:
    config.read('keys')
  # check for losing main or sub title  
  except (configparser.MissingSectionHeaderError, configparser.ParsingError):
    print('Format of files is not qualified, will use previous JSON file instead')
    # call function for saved json file
    get_oldJson(twitterUsr)
    return 
  finally:
    print('Checking the contents') 

  auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(),config.get('auth', 'consumer_secret').strip())
  auth.set_access_token(config.get('auth', 'access_token').strip(),config.get('auth', 'access_secret').strip())

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

  # save json file
  tweetcontent= []
  for status in tweepy.Cursor(api.user_timeline,id=twitterUsr,count = 20,tweet_mode='extended').items(20):
    tweetcontent.append(status.full_text)

  #write tweet objects to JSON
  file = open('jsonFolder/' + twitterUsr+'.json', 'w')
  print ("Writing tweet objects to JSON file, please wait...")
  json.dump(tweetcontent,file,indent = 4)
  print ("Done")
  file.close()

## test only
tweepy_info("BU_ece")
