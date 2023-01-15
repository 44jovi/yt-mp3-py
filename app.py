import youtube_dl
import glob
import os
from pydub import AudioSegment


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


def get_trimmed(mp3_filename, start, end=""):
    if (not mp3_filename):
        raise Exception("No .mp3 found in directory.")
    sound = AudioSegment.from_mp3(mp3_filename)
    t0 = get_video_time_milliseconds(start)
    print("Trimming file, ", mp3_filename, ".\n")
    print("Starting from ", start, "...")
    if (len(end) > 0):
        print("... up to ", end, ".\n")
        t1 = get_video_time_milliseconds(end)
        return sound[t0: t1]
    return sound[t0:]


def main():
    # WIP: Convert to user CLI to avoid hard-coding
    youtube_url = "https://youtu.be/OBLkvpBHLkc"
    download_audio(youtube_url)


# Execute
main()
