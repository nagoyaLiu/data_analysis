import json
from googleapiclient.discovery import build
import sys

args = sys.argv
SEARCH_CHANNEL_ID = args[1]

API_KEY = 'AIzaSyCl2b0TRL4emhOE1J5TLSetMnTFbHIzCWQ'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
youtube = build(
   YOUTUBE_API_SERVICE_NAME,
   YOUTUBE_API_VERSION,
   developerKey=API_KEY
)

response = youtube.search().list(
   part = "snippet",
   channelId = SEARCH_CHANNEL_ID,
   maxResults = 1,
   order = "date"
   ).execute()

for item in response.get("items", []):
   if item["id"]["kind"] != "youtube#video":
       continue
   print(json.dumps(item, indent=2, ensure_ascii=False))