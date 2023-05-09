from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import yt_dlp

download_dir = ""

def video_downloader(urls):
        ydl_opts = {
            'outtmpl': f'{download_dir}/%(title)s.%(ext)s',
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(urls)
        except:
            print("Failed to download.")

def audio_downloader(urls):
        ydl_audio_opts = {
            'format': 'm4a/bestaudio/best',
            'outtmpl': f'{download_dir}/%(title)s.%(ext)s',
            # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
            'postprocessors': [{  # Extract audio using ffmpeg
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }]
        }
        try:
            print("Downloading...")
            with yt_dlp.YoutubeDL(ydl_audio_opts) as ydl:
                ydl.download(urls)
        except:
            print("Failed to download.")

def choose_download_dir():
    # created global variable so that I can set the download director in functions audio_downloader 
    # and video_downloader without having to be prompted at least twice for the downloaded directory.
    global download_dir
    download_dir = filedialog.askdirectory()
    ttk.Label(mainframe, text=download_dir).grid(column=3, row=4, sticky=W)
    return download_dir

def downloader():
    URLS = url_entry.get()
    vbox_state = vidaud_bool.get()
    abox_state = aud_bool.get()

    print(vbox_state)
    print(abox_state)
    if (vbox_state == True):
        video_downloader(URLS)
    if (abox_state == True):
        audio_downloader(URLS)

# Creating GUI
root = Tk()
root.title("Downloader")
icon = tk.PhotoImage(file="assets/dl.png")
root.wm_iconphoto(True, icon)

# GUI Frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Entry label
ttk.Label(mainframe, text="URL:").grid(column=2, row=1,sticky=(W, E))

# Creating Entry box
input_url = StringVar()
url_entry = ttk.Entry(mainframe, width=48, textvariable=input_url)
url_entry.grid(column=3, row=1, sticky=(W, E))

# creating check box for video/audio or audio
vidaud_bool = BooleanVar()
aud_bool = BooleanVar()
ttk.Checkbutton(mainframe, text="Video/Audio", variable=vidaud_bool).grid(column=2, row=2, sticky=W)
ttk.Checkbutton(mainframe, text="Audio", variable=aud_bool).grid(column=2, row=3, sticky=W)

# Download button
ttk.Button(mainframe, text="Download", command=downloader).grid(column=5, row=5, sticky=W)

# Download Directory
ttk.Button(mainframe, text="Select a directory", command=choose_download_dir).grid(column=2, row=4, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

url_entry.focus()
root.bind("<Return>", downloader)

root.mainloop()