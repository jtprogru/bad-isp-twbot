#!/usr/bin/env python3
# coding=utf-8
# Created by JTProgru
# Date: 2017
# Simple Twitter-bot for posting
# speedtest information about my work ISP
# https://jtprog.ru/

__author__ = 'jtprogru'
__version__ = '0.0.1'
__author_email__ = 'mail@jtprog.ru'

import os
import csv
import datetime
import time
import twitter
import dotenv as d
from pathlib import Path


env = d.get_variables(str(Path(__file__).parent / '.env'))

# tweet_speed = f'My speedtest now is: {0}'  # \n Hey! {env["MY_ISP_TW"]}'


def test_speed():
    # run speedtest-cli
    print("running test speed")
    resp = os.popen("python speedtest-cli --simple").read()
    print('ran')
    # split the 3 line result (ping,down,up)
    lines = resp.split('\n')
    print(resp)
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    # if speedtest could not connect set the speeds to 0
    if "Cannot" in resp:
        ping = 100
        dowloadspeed = 0
        uploadspeed = 0
    # extract the values for ping down and up values
    else:
        ping = lines[0][6:11]
        dowloadspeed = lines[1][10:15]
        uploadspeed = lines[2][8:12]
    print(date, ping, dowloadspeed, uploadspeed)
    # save the data to file for local network plotting
    out_file = open('data.csv', 'a')
    writer = csv.writer(out_file)
    writer.writerow((ts * 1000, ping, dowloadspeed, uploadspeed))
    out_file.close()

    my_auth = twitter.OAuth(env['TOKEN'], env['TOKEN_KEY'], env['CON_SEC'], env['CON_SEC_KEY'])
    twit = twitter.Twitter(auth=my_auth)

    # try to tweet if speedtest couldnt even connet.
    # probably wont work if the internet is down

    if "Cannot" in resp:
        try:
            tweet_status = "WTF, что с моим интернетом? #JTProgru #"
            twit.statuses.update(status=tweet_status)
        except Exception as e:
            print(str(e))
            pass

    # tweet if down speed is less than whatever I set
    elif eval(dowloadspeed) < eval(env['ISP_PAYED_SPEED']):
        print(eval(dowloadspeed))
        print(eval(uploadspeed))
        print(eval(env['ISP_PAYED_SPEED']))
        print("trying to tweet")
        try:
            # i know there must be a better way than to do (str(int(eval())))
            tweet = str(float(eval(dowloadspeed))) + " down\\" + str(float(eval(uploadspeed))) + " up #speedtest"
            twit.statuses.update(status='My speedtest now is: ' + tweet)
        except Exception as e:
            print(str(e))
    return


if __name__ == '__main__':
    test_speed()
    print('completed')
