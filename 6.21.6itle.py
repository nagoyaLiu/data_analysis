import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#API_KEY = 'AIzaSyCl2b0TRL4emhOE1J5TLSetMnTFbHIzCWQ'#劉建
#API_KEY = 'AIzaSyBEBkplR8T-Yqjp8mIajT-bzq6TajtbAJA' #易欣欣
#API_KEY='AIzaSyD0rXAuO6p2OkDoSLURDT_0ggGqTTA3DBo' #tyou
API_KEY='AIzaSyAWeb1DyYIUAkOp7JEiBYNhk2tSrav_hww' #黄
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
CHANNEL_ID = 'UCgMPP6RRjktV7krOfyUewqw'
channels = [] #チャンネル情報を格納する配列
searches = [] #videoidを格納する配列
videos = [] #各動画情報を格納する配列
nextPagetoken = None
nextpagetoken = None

youtube = build(
    YOUTUBE_API_SERVICE_NAME, 
    YOUTUBE_API_VERSION,
    developerKey=API_KEY
    )

channel_response = youtube.channels().list(
    part = 'snippet,statistics',
    id = CHANNEL_ID
    ).execute()
  
# for channel_result in channel_response.get("items", []):
#     if channel_result["kind"] == "youtube#channel":
#         channels.append([channel_result["snippet"]["title"],channel_result["statistics"]["subscriberCount"],channel_result["statistics"]["videoCount"],channel_result["snippet"]["publishedAt"]])

while True:
    if nextPagetoken != None:
        nextpagetoken = nextPagetoken

    search_response = youtube.search().list(
      part = "snippet",
      channelId = CHANNEL_ID,
      maxResults = 50,
      order = "date", #日付順にソート
      pageToken = nextpagetoken #再帰的に指定
      ).execute()  

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            searches.append(search_result["id"]["videoId"])

    try:
        nextPagetoken =  search_response["nextPageToken"]
    except:
        break
   
for result in searches:
    video_response = youtube.videos().list(
      part = 'snippet,statistics,contentDetails',
      id = result
      ).execute()

    for video_result in video_response.get("items", []):
        if video_result["kind"] == "youtube#video":
            videos.append([video_result["snippet"]["title"],#video_result["statistics"]["viewCount"],
            #video_result["statistics"]["likeCount"],
            video_result["snippet"]["publishedAt"],video_result["contentDetails"]["duration"]])  

videos_report = pd.DataFrame(videos, columns=['title',#'viewCount',
 #'likeCount',
  'publishedAt', 'duration'])
videos_report.to_csv("videos_reportNo1.csv", index=None, encoding='utf-8')

# channel_report = pd.DataFrame(channels, columns=['title', 'subscriberCount', 'videoCount', 'publishedAt'])
# channel_report.to_csv("channels_report6.csv", index=None, encoding='utf-16')

# video_result["statistics"]["commentCount"],'commentCount',video_result["statistics"]["viewCount"],video_result["statistics"]["likeCount"],