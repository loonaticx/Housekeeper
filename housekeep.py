"""
Author: Ryan Walters

This program resizes images to power of 2 for use in game engines.

Original Repository URL: https://github.com/RyanAWalters/PowerOf2ImageResizer

Modified 9/20/21 by Loonatic

This modified version was built for managing and optimizing Toontown resources, including content packs.
"""

from __future__ import print_function
import io
import sys
from PIL import Image
from PIL import ImageCms


sizes = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]  # po2 sizes
# Don't include 2 since panda doesn't like that res
# Nothing should EVER be considered to be higher than 2048 in res for Toontown.

def get_closest(y):
    """ Return the closest power of 2 in either direction"""
    return min(sizes, key=lambda x: abs(x - y))


def po2(im):
    """
    Return a resized image that is a power of 2, modified to ignore
    a need of a threshold, also converts wrt each dimension (ex: 1024x512)
    """
    name = im.filename
    width, height = im.size
    new_dimX = get_closest(width)
    new_dimY = get_closest(height)
    if not width == new_dimX:
        print("Warning: {} width not po2: {}, resizing to {}".format(name, width, new_dimX))
    if not height == new_dimY:
        print("Warning: {} height not po2: {}, resizing to {}".format(name, height, new_dimY))
    return im.resize((new_dimX, new_dimY))

# https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes

def checkColorMode(im):
    cmode = im.mode
    name = im.filename
    if not cmode == 'RGB' and not cmode == 'RGBA':
        print("Info: File {} from {} is not RGB/RGBA color mode".format(name, cmode))
        #im = im.convert('RGB')

def checkICCProfile(im):
    # https://stackoverflow.com/questions/31865743/pil-pillow-decode-icc-profile-information
    # https://pillow.readthedocs.io/en/stable/reference/ImageCms.html#PIL.ImageCms.CmsProfile
    name = im.filename
    icc = im.info.get('icc_profile')
    if icc is not None:
        print("Warning: {} has icc data, will be removed".format(name))

# todo: migrate out of sys.argv land
class Housekeep():
    def __init__(self, files):
        """
        Driver code
        Compression ranges from 0 to 9, 0 = no compression and 9 is max,
        PIL's default is 6
        """
        compression = 9
        opt = True
        try:
            for file in files:
                try:
                    im = Image.open(file)
                    ft = im.format.upper()
                    checkICCProfile(im)
                    checkColorMode(im)
                    if ft == "JPEG" or ft == "JPG":
                        po2(im).save(file, quality=100, subsampling=0)
                    elif ft == "PNG":
                            if opt:
                                po2(im).save(file, icc_profile=None, compress_level=compression, format='PNG', optimize=True)
                    else:
                        po2(im).save(file)
                except IOError:
                    print("IO ERROR: Is file an image? -> ", file)
        except MemoryError:
            print("Error: out of memory.")

