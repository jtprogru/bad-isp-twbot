#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2017 Savin Mihael
# Simple Twitter-bot for posting
# speedtest information about my work ISP


import os
import csv
import datetime
import time
import twitter
import dotenv as d
from pathlib import Path


env = d.get_variables(str(Path(__file__).parent / '.env'))

tweet_speed = f'My speedtest now is: {0} \n Hey! {env["MY_ISP_TW"]}'


def test():
    # run speedtest-cli
    print("running test")
    a = os.popen("python speedtest-cli --simple").read()
    print('ran')
    # split the 3 line result (ping,down,up)
    lines = a.split('\n')
    print(a)
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    # if speedtest could not connect set the speeds to 0
    if "Cannot" in a:
        p = 100
        d = 0
        u = 0
    # extract the values for ping down and up values
    else:
        p = lines[0][6:11]
        d = lines[1][10:14]
        u = lines[2][8:12]
    print(date, p, d, u)
    # save the data to file for local network plotting
    out_file = open('data.csv', 'a')
    writer = csv.writer(out_file)
    writer.writerow((ts * 1000, p, d, u))
    out_file.close()

    my_auth = twitter.OAuth(env['TOKEN'], env['TOKEN_KEY'], env['CON_SEC'], env['CON_SEC_KEY'])
    twit = twitter.Twitter(auth=my_auth)

    # try to tweet if speedtest couldnt even connet.
    # probably wont work if the internet is down

    if "Cannot" in a:
        try:
            tweet_status = "WTF, что с моим интернетом? #JTProgru "
            twit.statuses.update(status=tweet_status)
        except:
            pass

    # tweet if down speed is less than whatever I set
    elif eval(d) < 65:
        print("trying to tweet")
        try:
            # i know there must be a better way than to do (str(int(eval())))
            tweet = str(int(eval(d))) + "down\\" + str(int(eval(u))) + "up #speedtest"
            twit.statuses.update(status=tweet_speed.format(tweet))
        except Exception as e:
            print(str(e))
            pass
    return


if __name__ == '__main__':
    test()
    print('completed')
