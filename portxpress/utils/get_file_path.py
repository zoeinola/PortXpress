import os

def get_filename(path): #/abc/filename.mp4
    return os.path.basename(path)


def get_filename(filename):
    return filename.upper()