#!/usr/bin/env python3

import configparser
import os
import tweepy
import random
print("Starting...")

api_key = ''
api_key_secret = ''
bearer_token = ''
access_token = ''
access_secret = ''

config = configparser.RawConfigParser()

config.read('/home/zack/tweepy_credentials')
api_key = config.get('default', 'api_key')
api_key_secret = config.get('default', 'api_key_secret') 
bearer_token = config.get('default', 'bearer_token') 
access_token = config.get('default', 'access_token') 
access_secret = config.get('default', 'access_secret')

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles

listOfFiles = getListOfFiles("/home/zack/MathQualBot/QualbotQuestions")
rfile = random.choice(listOfFiles)
api.update_with_media(rfile, status="Testing scheduled tweets with pictures:")
#api.update_status("Testing scheduled tweets.")
print("Done for the day!")
