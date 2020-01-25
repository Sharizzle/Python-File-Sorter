import shutil
import os

'''
Folders and Extensions:

Documents - doc,docx,txt,pdf
Video - mkv,mp4,webm,mov,avi,m4v
Audio - mp3,wav,flac,
Images - psd,jpg,png,tiff,bmp,
Zip Files - zip,rar,7z,iso
Code - html,css,py,js,php,rb,xml,json,pyw,c,sh,bat,cs,java
Other
Folders

'''

extensions = {
    "Documents": ["doc", "docx", "txt", "pdf"],
    "Video": ["mkv", "mp4", "webm", "mov", "avi", "m4v"],
    "Audio": ["mp3", "wav", "flac"],
    "Images": ["psd", "jpg", "png", "tiff", "bmp"],
    "Zip Files": ["zip", "rar", "7z", "iso"],
    "Code": ["html", "css", "py", "js", "php", "rb", "xml",
             "json", "pyw", "c", "sh", "bat", "cs", "java"],
    "Folders": [],
    "Other": []

}


def sort_files(path, extensions):

    files = os.listdir(path)

    try:
        for folder in extensions.keys():
            os.mkdir(folder)
    except FileExistsError:
        pass

    dont_Touch = extensions.keys()

    for file in files:
        try:
            is_found = False
            ext = os.path.splitext(file)[1]
            ext = ext[1:]
            if os.path.isdir(file):
                if file in dont_Touch:
                    pass
                else:
                    shutil.move(file, "Folders")
            else:
                for key, value in extensions.items():
                    if os.path.splitext(file)[0] == "sorter":
                        is_found = True
                        raise Exception()
                    elif ext in value:
                        shutil.move(file, key)
                        is_found = True
                        raise Exception()
                if not is_found:
                    shutil.move(file, "Other")
                    raise Exception()
        except:
            pass


sort_files(r".", extensions)
