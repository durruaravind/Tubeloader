from tkinter import *
from pytube import YouTube
from datetime import datetime

window = Tk()
window.geometry("720x400")
window.config(bg="ROYAL BLUE")
window.title("ytb-downloader")
window.resizable(0,0)
youtube_logo = PhotoImage(file = "youtube-logo.png")
window.iconphoto(False, youtube_logo)

Label(window, text = " YOUTUBE VIDEO DOWNLOADER PROJECT ", font = ("Courier", 20, "bold"), bg = "WHITE").pack(padx = 5, pady = 50)
Video_Link = StringVar()
Label(window, text = " URL ", font = ("Roboto", 14, "bold"), bg = "WHITE").place(x= 45, y = 125)
Entry_Link = Entry(window, width = 50, font = 24, textvariable = Video_Link).place(x = 105, y = 125)

# code for creating the checkbox form
filetypevalue_mp4 = IntVar()
filetype_mp4 = Checkbutton(text = "MP4", variable = filetypevalue_mp4).place(x = 300, y = 175)
filetypevalue_mp3 = IntVar()
filetype_mp3 = Checkbutton(text = "MP3", variable = filetypevalue_mp3).place(x = 350, y = 175)

# according to the value entered in checkbox, appropriate commands are excecuted
def getfiletype():
    if(filetypevalue_mp4.get() == 1 & filetypevalue_mp3.get() == 1):
        video_download()
        audio_download()
    else:
        if(filetypevalue_mp4.get() == 1):
            video_download()
        if(filetypevalue_mp3.get() == 1):
            audio_download()

# code for downloading the mp4 video at highest resolution
def video_download():
    video_url = YouTube(str(Video_Link.get()))
    video = video_url.streams.get_highest_resolution()
    path = 'E:\Python Projects\YTB_Downloader\Downloaded Videos'
    video.download(path)
    Label(window, text = "MP4 Video Download Completed!", font = ("Roboto", 14, "bold"), bg = "ROYAL BLUE", fg = "WHITE").place(x = 200, y = 300)
    Label(window, text = "CHECK YOUR PROJECT FOLDER", font = ("Roboto", 14, "bold"), bg = "ROYAL BLUE", fg = "WHITE").place(x = 200, y = 325)

    # writing the details of the download in history.txt as a record
    with open("history.txt", "a") as f:
        now = datetime.now()
        dateandtime = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write("MP4        ")
        f.write(video.title)
        f.write("       ")
        f.write(dateandtime)
        f.write("       Thumbnail  ")
        f.write(video_url.thumbnail_url)
        f.write("\n")

# code for downlading the mp3 audio
def audio_download():
    video_url = YouTube(str(Video_Link.get()))
    audio = video_url.streams.get_audio_only()
    path = 'E:\Python Projects\YTB_Downloader\Downloaded Audios'
    audio.download(path)
    Label(window, text = "MP3 Audio Download Completed!", font = ("Roboto", 14, "bold"), bg = "ROYAL BLUE", fg = "WHITE").place(x = 200, y = 300)
    Label(window, text = "CHECK YOUR PROJECT FOLDER", font = ("Roboto", 14, "bold"), bg = "ROYAL BLUE", fg = "WHITE").place(x = 200, y = 325)

    # writing the details of the download in history.txt as a record
    with open("history.txt", "a") as f:
        now = datetime.now()
        dateandtime = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write("MP3        ")
        f.write(audio.title)
        f.write("       ")
        f.write(dateandtime)
        f.write("       Thumbnail  ")
        f.write(video_url.thumbnail_url)
        f.write("\n")

# Download button
Button(window, text = "DOWNLOAD", font = ("Roboto", 24, "bold"), bg = "LIGHTBLUE", command = getfiletype).place(x= 240, y = 225)
window.mainloop()