import youtube_dl
import video_to_ascii

def play(video_uri):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_uri])
