import os
import shutil
from datetime import datetime
import PIL.Image

extensions = ['jpg', 'png', 'jpeg', 'JPG', 'PNG', 'JPEG']


def folder_path_from_photo_date(file):
    date = photo_shooting_date(file)
    return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')


def photo_shooting_date(file):
    img = PIL.Image.open(file)
    info = img._getexif()
    if info and 36867 in info:
        date = info[3687]
        date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
    else:
        date = datetime.fromtimestamp(os.path.getatime(file))
    return date


def move_photo(file):
    new_folder = folder_path_from_photo_date(file)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    shutil.move(file, new_folder + '/' + file)


def organize():
    photos = [
        filename for filename in os.listdir('.') if any(
            filename.endswith(ext) for ext in extensions)
    ]
    for filename in photos:
        move_photo(filename)


print(organize())
# print(move_photo('user.png'))
# print(move_photo("view_model.jpg"))