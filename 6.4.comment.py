
from apiclient.discovery import build
API_KEY = 'AIzaSyCl2b0TRL4emhOE1J5TLSetMnTFbHIzCWQ'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(
    YOUTUBE_API_SERVICE_NAME, 
    YOUTUBE_API_VERSION,
    developerKey=API_KEY
    )

search_response = youtube.search().list(
  q='[マナブ]',
  part='id,snippet',
  maxResults=25
).execute()

channels = []

for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#channel":
        channels.append([search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]])
                                  
for channel in channels:
print(channel)