import os
import tkinter as tk
from tkinter import filedialog

# This will correct he blury font issue in Windows 10
if os.name == "nt":
    from ctypes import windll, pointer, wintypes
    try:
        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass  # this will fail on Windows Server and maybe early Windows

# eg C:\Users\User\Music\Barbra Streisand\A Collection- Greatest Hits... And More
# https://datatofish.com/rename-file-python/
# rename files to get rid of numbers in front of them


def formatMp3(directory):
    fileCount = 0
    for filename in os.listdir(directory):
        if filename.lower().endswith(".mp3"):
            if(filename[0].isdigit() and filename[1].isdigit()):
                new_file_name = filename[3:].lstrip()
                old_path_to_file = directory + "/" + filename
                new_path_to_file = directory + "/" + new_file_name
                os.rename(old_path_to_file, new_path_to_file)
                fileCount += 1
    stateLbl['text'] = '{} MP3s Corrected'.format(fileCount)


def locationPath():  # Create File Dialog to to select folder
    value = filedialog.askdirectory(
        initialdir=os.getcwd(), title="Select Location")
    locationEntry.delete(0, "end")
    locationEntry.insert(0, value)
    misLabled = 0
    for filename in os.listdir(value):
        if filename.lower().endswith(".mp3"):
            if(filename[0].isdigit() and filename[1].isdigit()):
                misLabled += 1
    stateLbl['text'] = '{} Mislabled MP3s Found'.format(misLabled)


# Setup Gui with Tkinter
window = tk.Tk()
window.resizable(width=False, height=False)
window.iconbitmap(False, 'icon.ico')
window.title("MP3 Format")
window.columnconfigure(2, weight=1, minsize=75)
window.rowconfigure(1, weight=1, minsize=50)

# Location selection
locationLbl = tk.Label(text='MP3s Location', anchor="e")
locationLbl.grid(row=0, column=0, padx=5, pady=5)
locationEntry = tk.Entry(width=25)
locationEntry.grid(row=0, column=1, padx=5, pady=5)
locationBtn = tk.Button(text="Select Location",
                        command=lambda: locationPath())
locationBtn.grid(row=0, column=2, padx=5, pady=5)

# Status
statusLbl = tk.Label(text='Status: ')
statusLbl.grid(row=1, column=0, padx=5, pady=5)

# State
stateLbl = tk.Label(text='Ready')
stateLbl.grid(row=1, column=1, padx=5, pady=5, sticky='w')

# Format Now Button
formatBtn = tk.Button(
    text="Format Now", command=lambda: formatMp3(locationEntry.get()))
formatBtn.grid(row=1, column=2, padx=5, pady=5, sticky='w')

window.mainloop()
