#!/usr/bin/env python
# coding=utf-8
# Created by JTProgru
# Date: 2019-08-13
# https://jtprog.ru/

__author__ = 'jtprogru'
__version__ = '0.0.1'
__author_email__ = 'mail@jtprog.ru'

import twitter
import dotenv as d
from pathlib import Path
from speedtest import Speedtest
import json

env = d.get_variables(str(Path(__file__).parent / '.env'))

servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

s = Speedtest()
# s.get_servers(servers)
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)
# s.results.json()

resp = json.loads(s.results.json(pretty=True))
print(resp)
print()
print('%.2f' % (resp['bytes_received'] / 1024 / 1024))

# my_auth = twitter.OAuth(env['TOKEN'], env['TOKEN_KEY'], env['CON_SEC'], env['CON_SEC_KEY'])
# twit = twitter.Twitter(auth=my_auth)

# try to tweet if speedtest couldnt even connet.
# probably wont work if the internet is down

# if "Cannot" in resp:
#     try:
#         tweet_status = "WTF, что с моим интернетом? #JTProgru #"
#         twit.statuses.update(status=tweet_status)
#     except Exception as e:
#         print(str(e))
#         pass

# tweet if down speed is less than whatever I set
# elif eval(resp['download']) < eval(env['ISP_PAYED_SPEED']):
#     print(eval(dowloadspeed))
#     print(eval(uploadspeed))
#     print(eval(env['ISP_PAYED_SPEED']))
#     print("trying to tweet")
#     try:
        # i know there must be a better way than to do (str(int(eval())))
        # tweet = str(float(eval(dowloadspeed))) + " down\\" + str(float(eval(uploadspeed))) + " up #speedtest"
        # twit.statuses.update(status='My speedtest now is: ' + tweet)
    # except Exception as e:
    #     print(str(e))

