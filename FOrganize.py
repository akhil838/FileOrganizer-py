# import OS module
import os

doc = {'.txt', '.docx', '.pdf', '.xlsx', '.pptx', '.doc', '.html', '.htm', '.odt', '.xls', '.ods', '.838', '.ppt'}
img = {'.heic', '.jpeg', '.jpg', '.png', '.gif', '.tiff', '.psd', '.eps', '.svg'}
vid = {'.mov', '.mp4', '.mkv', '.avi', '.wmv', '.avchd', '.webm', '.flv'}
audio = {'.mp3','.pcm','.wav','.aiff','.aac','.ogg','.wma','.flac','.alac'}

#   Taking Input for path
path = input("Enter Path TO Folder: ")
dir_list = os.listdir(path)

#   Creating The DIR to sort
print('CREATING NECESSARY DIRECTORIES\n')
try:
    os.mkdir(path + '\\DOCS')
except OSError as error:
    print('DOCS Directory already exists')
try:
    os.mkdir(path + '\\Images')
except OSError as error:
    print('Images Directory already exists')
try:
    os.mkdir(path + '\\Videos')
except OSError as error:
    print('Videos Directory already exists')
try:
    os.mkdir(path + '\\Audios')
except OSError as error:
    print('Audios Directory already exists')

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

print('\nFiles SORTED SUCCESSFULLY')
