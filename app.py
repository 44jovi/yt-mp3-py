import youtube_dl
import glob
import os


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


def latest_mp3_filename():
    mp3s_list = glob.glob('./*.mp3')
    return max(mp3s_list, key=os.path.getctime)


def main():
    # WIP: Convert to user CLI to avoid hard-coding
    youtube_url = "https://youtu.be/OBLkvpBHLkc"
    download_audio(youtube_url)


# Execute
main()
