import youtube_dl
def youtubeDownload():
    save_path = "your own path"
    # outtmpl help navigate your path where you want to save your file
    # after downloading from youtube
    ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': save_path + '%(title)s.%(ext)s',
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',}],
        }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(["https://www.youtube.com/watch?v=cxZ-x84HwHU"])
    except FileNotFoundError as fnf_error:
        print("file not found ")

if __name__ == '__main__':
    youtubeDownload()
