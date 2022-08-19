import pandas as pd

# hololive ホロライブ - VTuber GroupのチャンネルID
cId = 'AIzaSyCl2b0TRL4emhOE1J5TLSetMnTFbHIzCWQ' 

# 動画情報を取得 
response = youtube.search().list(
    # 検索部分を指定
    part = "snippet", 
    # チャンネルID 
    channelId = cId, 
    # 検索数 
    maxResults = 10, 
    # 検索順(今回は日付) 
    order = "date" ).execute()

data = []

for vdata in response['items']:
    count_data = youtube.videos().list(
        part = 'statistics', 
        id = vdata['id']['videoId']
    ).execute()['items'][0]['statistics'] 
    pub_date = vdata['snippet']['publishedAt'] 
    v_title = vdata['snippet']['title']
    v_count = int(count_data['viewCount'])
    v_like = int(count_data['likeCount'])
    v_dislike = int(count_data['dislikeCount'])
    data.append([pub_date,v_title,v_count,v_like,v_dislike])
data = pd.DataFrame(data,columns=['date','title','count','like','dislike'])
data.to_csv('youtube.csv')