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


def get_video_time_milliseconds(video_time):
    # Split video time ("HH:MM:SS" or "MM:SS") into an array
    video_time_to_array = video_time.split(":")
    # If "HH:MM:SS"
    if (len(video_time_to_array) == 3):
        hours = int(video_time_to_array[0]) * 60 * 60 * 1000
        minutes = int(video_time_to_array[1]) * 60 * 1000
        seconds = int(video_time_to_array[2]) * 1000
    # Else if "MM:SS"
    else:
        hours = 0
        minutes = int(video_time_to_array[0]) * 60 * 1000
        seconds = int(video_time_to_array(1)) * 1000
    # Return time in milliseconds
    return hours + minutes + seconds


def main():
    # WIP: Convert to user CLI to avoid hard-coding
    youtube_url = "https://youtu.be/OBLkvpBHLkc"
    download_audio(youtube_url)


# Execute
main()
