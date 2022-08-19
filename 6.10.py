import os
import time
import requests

import pandas as pd
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
#CHANNEL_ID = 'UCibEhpu5HP45-w7Bq1ZIulw'
channels = [] #チャンネル情報を格納する配列
searches = [] #videoidを格納する配列
videos = [] #各動画情報を格納する配列
nextPagetoken = None
nextpagetoken = None
API_KEY = 'AIzaSyBEBkplR8T-Yqjp8mIajT-bzq6TajtbAJA'
youtube = build(
    YOUTUBE_API_SERVICE_NAME, 
    YOUTUBE_API_VERSION,
    developerKey=API_KEY
    )

CHANNEL_ID = 'UC6qqQP2idQCBOCZrkemR9tw'

base_url = 'https://www.googleapis.com/youtube/v3'
url = base_url + '/search?key=%s&channelId=%s&part=snippet,id&order=date&maxResults=50'
infos = []
count_data =[]
while True:
    time.sleep(30)
    response = requests.get(url % (API_KEY, CHANNEL_ID))
    if response.status_code != 200:
        print('エラーで終わり')
        break
    result = response.json()
    infos.extend([
        [item['id']['videoId'], item['snippet']['title'] #item['statistics']['likeCount']
        ]
        for item in result['items'] if item['id']['kind'] == 'youtube#video'
    ])

    if 'nextPageToken' in result.keys():
        if 'pageToken' in url:
            url = url.split('&pageToken')[0]
        url += f'&pageToken={result["nextPageToken"]}'
    else:
        print('正常終了')
        break
    for vdata in infos['items']:
       count_data = youtube.videos().list(part = 'statistics', id = vdata['id']['videoId']).execute()['items'][0]['statistics']
       print('再生回数：',count_data['viewCount'],'高評価数：',count_data['likeCount'])
videos = pd.DataFrame(infos, columns=['videoId',
 'title'
 #'viewCount'
 #'publishedAt'
 ])
videos.to_csv('videosNo 12.csv', index=None)
#print(count_data)

# item['snippet']['description'],