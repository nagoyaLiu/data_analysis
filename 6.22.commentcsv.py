import requests
import json
import os
import time
import requests

import pandas as pd
URL = 'https://www.googleapis.com/youtube/v3/'
API_KEY = 'AIzaSyCl2b0TRL4emhOE1J5TLSetMnTFbHIzCWQ'

def print_video_comment(video_id, n=10):
    params = {
        'key': API_KEY,
        'part': 'snippet',
        'videoId': video_id,
        'order': 'relevance',
        'textFormat': 'plaintext',
        'maxResults': n,
    }
    response = requests.get(URL + 'commentThreads', params=params)
    resource = response.json()
 
    for comment_info in resource['items']:
        # コメント
        text = comment_info['snippet']['topLevelComment']['snippet']['textDisplay']
        # グッド数
        like_cnt = comment_info['snippet']['topLevelComment']['snippet']['likeCount']
        # 返信数
        reply_cnt = comment_info['snippet']['totalReplyCount']


        print('{}\n g: {}h : {}\n'.format(text, like_cnt, reply_cnt))
       
video_id = '  7p7mpahlv8Y  '
    
print_video_comment(video_id, n=10)

#open_file = open('append.txt','a')
#open_file.write(f'{print_video_comment()}')
#open_file.close()