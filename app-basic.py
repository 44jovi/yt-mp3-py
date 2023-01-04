import youtube_dl

# Basic version with only core function of converting YouTube video to .mp3 format


def download_audio(youtube_url):
    yt_dl_options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(yt_dl_options) as yt_dl:
        yt_dl.download([youtube_url])


download_audio("https://youtu.be/OBLkvpBHLkc")
