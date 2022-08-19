import os
from googleapiclient.discovery import build

api_key = 'AIzaSyCl2b0TRL4emhOE1J5TLSetMnTFbHIzCWQ'

youtube = build('youtube','v3',developerKey=api_key)

pl_request = youtube.channels().list(
        part='contentdetails,snippet',
        id='UC_JZnNZYndljN3qqnecYUEA'
    )

pl_response = pl_request.execute()

for item in pl_response['item']:
    print(item)
    print()