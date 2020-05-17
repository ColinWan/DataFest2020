import os
from twarc import Twarc
import sys
import json
import numpy as np
import pandas as pd

def pull_tweet(input_file_name):
    CONSUMER_KEY = "9At2u3Y2DraTHLSg3D9w6LhE9"
    CONSUMER_KEY_SECRET = "DRFCbI2t0gMhfV2KnEub6cljowW9zRwmkeMJ0GT9MlMkrkzspM"
    ACCESS_TOKEN = "1259913765614751745-LwtSI48si3sYekzvxW86syIFsRgirl"
    ACCESS_TOKEN_SECRET = "e0gpJdT0IXOSxFrhplKMl8FlP0dVnuLg1vwBHzt5Fc9J9"

    t = Twarc(CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    inputF = open(input_file_name, "r")
    line = inputF.readline()
    data = []
    i=0
    while line != "" and i<10:
        try:
            tweet = t.tweet(line.strip())
            if tweet["lang"] == "en":
                if 'retweeted_status' in tweet.keys():
                    data.append(tweet['retweeted_status']['full_text'].replace('\n', ' '))
                else:
                    data.append(data, tweet['full_text'].replace('\n', ' '))
                i += 1
            line = inputF.readline()
        except Exception as e:
            line = inputF.readline()
    return data


def write_tweet_to_csv(input_file_name, output_file_name):
    data = pull_tweet(input_file_name)
    df = pd.DataFrame(data, columns=[input_file_name[-17:-4]])
    df.to_csv(output_file_name, index=False)

input_file_name = '/Users/colinwan/Desktop/DataFest2020/Tweets/coronavirus-through-1-May-2020-00.txt'
output_file_name = '/Users/colinwan/Desktop/DataFest2020/Tweets/test.csv'