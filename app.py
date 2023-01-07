import youtube_dl


def download_audio(youtube_url):
    yt_dl_options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(yt_dl_options) as yt_dl:
        yt_dl.download([youtube_url])


def main():
    # WIP: Convert to user CLI to avoid hard-coding
    youtube_url = "https://youtu.be/OBLkvpBHLkc"
    download_audio(youtube_url)


# Execute
main()
