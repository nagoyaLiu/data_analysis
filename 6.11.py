import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#API_KEY = 'AIzaSyCl2b0TRL4emhOE1J5TLSetMnTFbHIzCWQ'#劉建
#API_KEY = 'AIzaSyBEBkplR8T-Yqjp8mIajT-bzq6TajtbAJA' #易欣欣
API_KEY='AIzaSyD0rXAuO6p2OkDoSLURDT_0ggGqTTA3DBo' #tyou
#API_KEY='AIzaSyAWeb1DyYIUAkOp7JEiBYNhk2tSrav_hww' #黄
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(
    YOUTUBE_API_SERVICE_NAME, 
    YOUTUBE_API_VERSION,
    developerKey=API_KEY
    )
cId = 'UCQs-tWGqacJ7vuuJDtXq28w'

# 動画情報を取得

response = youtube.search().list(
    # 検索部分を指定
    part = "snippet",
    # チャンネルID
    channelId = cId,
    # 検索数
    maxResults = 50,
    # 検索順(今回は日付)
    
    order = "searchSortUnspecified"  #"date"'searchSortUnspecified', 'date', 'rating', 'viewCount', 'relevance', 'title', 'videoCount'
).execute()






infos =[]
videos =[]
for vdata in response['items']:
    count_data = youtube.videos().list(part = 'statistics', id = vdata['id']['videoId']).execute()['items'][0]['statistics']
    details_data= youtube.videos().list(part='contentDetails',id = vdata['id']['videoId']).execute()['items'][0]['contentDetails']
    #print('投稿日:',vdata['snippet']['publishedAt'])
    # infos.extend([count_data['likeCount']])
    # videos =pd.DataFrame( infos, columns=['likecount'] )
    # videos.to_csv('11.csv' ,index =None)
    infos.append([vdata['snippet']['title'],vdata['snippet']['publishedAt'],count_data['likeCount'],count_data['viewCount'],details_data['duration']])
    # print('動画名:',vdata['snippet']['title'])
    # print('再生回数：',count_data['viewCount'],'高評価数：',count_data['likeCount']
    # ,'低評価数：',count_data['dislikeCount'],
    # )
    # print('-----------------------------------------------------------------')
videos = pd.DataFrame(infos,columns=['title','publishedAt','likecount','viewcount','duration'])
videos.to_csv('任意抽出NO2.csv',index =None)
#print(infos)