# import OS module
import os

from tkinter import *
from tkinter import filedialog

path = NONE

#FILE EXTENTIONS LIST
doc = {'.txt', '.docx', '.pdf', '.xlsx', '.pptx', '.doc', '.html', '.htm', '.odt', '.xls', '.ods', '.838', '.ppt'}
img = {'.heic', '.jpeg', '.jpg', '.png', '.gif', '.tiff', '.psd', '.eps', '.svg'}
vid = {'.mov', '.mp4', '.mkv', '.avi', '.wmv', '.avchd', '.webm', '.flv'}
audio = {'.mp3', '.pcm', '.wav', '.aiff', '.aac', '.ogg', '.wma', '.flac', '.alac'}


def selectFolder():
    global path
    path = filedialog.askdirectory(initialdir="C:\\")
    text.delete('1.0', 'end')
    text.insert(INSERT, path)


def sort():
    dir_list = os.listdir(path)

    text.delete('1.0', 'end')
    #   Creating The DIR to sort
    text.insert(INSERT, 'CREATING NECESSARY DIRECTORIES\n')
    try:
        os.mkdir(path + '\\DOCS')
    except OSError as error:
        text.insert(INSERT, 'DOCS Directory already exists\n')
    try:
        os.mkdir(path + '\\Images')
    except OSError as error:
        text.insert(INSERT, 'Images Directory already exists\n')
    try:
        os.mkdir(path + '\\Videos')
    except OSError as error:
        text.insert(INSERT, 'Videos Directory already exists\n')
    try:
        os.mkdir(path + '\\Audios')
    except OSError as error:
        text.insert(INSERT, 'Audios Directory already exists\n')

    #   Sorting Files based on Extension
    for file in dir_list:
        for name in doc:
            if file.endswith(name):
                os.rename(path + '\\' + file, path + '\\DOCS\\' + file)
        for name in img:
            if file.endswith(name):
                os.rename(path + '\\' + file, path + '\\Images\\' + file)
        for name in vid:
            if file.endswith(name):
                os.rename(path + '\\' + file, path + '\\Videos\\' + file)
        for name in audio:
            if file.endswith(name):
                os.rename(path + '\\' + file, path + '\\Audios\\' + file)

    text.insert(INSERT, "FILES Organised")

#GUI
window = Tk()

window.title("File Organiser")
window.geometry("300x200+800+450")
window.resizable(width=False, height=False)

msg = Label(window, text="Select the Folder to Organise")
button = Button(text="1. Select Folder", command=selectFolder)
text = Text(window, width=35, height=6)
organise = Button(text="2. Organise", command=sort)
msg2 = Label(window, text="Made with ❤️\nakhil838")

msg.pack()
button.pack()
text.pack()
organise.pack()
msg2.pack()

window.mainloop()
