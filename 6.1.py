youtube = build('youtube','v3',
				developerKey="AIzaSyCl2b0TRL4emhOE1J5TLSetMnTFbHIzCWQ")

# retrieve youtube video results
video_response=youtube.commentThreads().list(
part='snippet,replies',
videoId="v=QzxmWzHtimA"
).execute()