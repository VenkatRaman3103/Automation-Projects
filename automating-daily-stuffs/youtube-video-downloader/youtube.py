from pytube import YouTube
from sys import argv

video_link = argv[1]
yt = YouTube(video_link)

print('Title: ', yt.title)
print('views: ', yt.views)

youtube_video = yt.streams.get_highest_resolution()

youtube_video.download('___Here mention the file directory___')