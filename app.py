import youtube_dl

def download_audio(youtube_url):
  yt_dl_options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
      }],
  }
  with youtube_dl.YoutubeDL(yt_dl_options) as ydl:
    ydl.download([youtube_url])

download_audio("https://youtu.be/OBLkvpBHLkc")

# WIP: Change URL argument to user CLI
