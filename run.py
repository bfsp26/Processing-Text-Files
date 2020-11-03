#! /usr/bin/env python3

import os
import requests
import json


def feedback_dct(path):
    files = os.listdir(path)
    feed_lst = []
    for file in files:
        with open(path + file) as fb_file:
            lines = fb_file.readlines()
            fb_dct = {
                "title": lines[0].strip(),
                "name": lines[1].strip(),
                "date": lines[2].strip(),
                "feedback": lines[3].strip()
            }
            feed_lst.append(fb_dct)
    return feed_lst


def upload_feedback(feed_lst, url):
    for feed in feed_lst:
        response = requests.post(url, json=feed)
        print(response.status_code)


def main():
    feedback_path='/data/feedback/'
    baseurl = r'http://<IP>/feedback/'
    feedback = feedback_dct(feedback_path)
    upload_feedback(feedback, baseurl)

 
main()

