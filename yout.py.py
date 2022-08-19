

from googleapiclient.discovery import build

API_KEY = 'AIzaSyCl2b0TRL4emhOE1J5TLSetMnTFbHIzCWQ'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
SEARCH_TEXT = 'jack'

youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developer=API_KEY
)

respose = youtube.seach().list(q=SEARCH_TEXT,part='id,snippet',maxResult=25).execute()

for item in respose.get('item',[]):
    if item['id']['kind'] != 'youtube#channel':
        continue
    print('*'* 10)
    print.dumps(item,indent=2,ensure_ascii=False))
    print('*'* 10)