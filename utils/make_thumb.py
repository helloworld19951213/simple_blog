import glob
import os

from PIL import Image

size = 128, 128


def create_thumb_pic(path, sort=0):
    """
    等比压缩
    :return:
    """
    for infile in glob.glob('media/' + str(path)):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(size)
        file_name = file.split('/')[-1]
        new_file = file.replace(file_name, 'thumb' + file_name)
        im.save(new_file + ext, "JPEG")
        return '/' + new_file + ext
