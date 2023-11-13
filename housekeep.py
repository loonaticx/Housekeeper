"""
Author: Ryan Walters

This program resizes images to power of 2 for use in game engines.

Original Repository URL: https://github.com/RyanAWalters/PowerOf2ImageResizer

Modified 9/20/21 by Loonatic

This modified version was built for managing and optimizing Toontown resources, including content packs.
"""

from __future__ import print_function
from PIL import Image

sizes = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]  # po2 sizes


# Don't include 2 since panda doesn't like that res
# Nothing should EVER be considered to be higher than 2048 in res for Toontown.

def get_closest(y):
    """ Return the closest power of 2 in either direction"""
    return min(sizes, key = lambda x: abs(x - y))


def get_po2_res(im):
    """
    Get dimensions for width height of the nearest power 2 resolution.
    """
    width, height = im.size
    return get_closest(width), get_closest(height)


def checkpo2(im):
    name = im.filename
    width, height = im.size
    new_dimX = get_closest(width)
    new_dimY = get_closest(height)
    if width == new_dimX and height == new_dimY:
        return False
    if not width == new_dimX:
        print("Warning: {} resizing width from {} to --> {}".format(name, width, new_dimX))
    if not height == new_dimY:
        print("Warning: {} resizing height from {} to --> {}".format(name, height, new_dimY))
    return True


def po2(im, alpha=True):
    """
    Return a resized image that is a power of 2, modified to ignore
    a need of a threshold, also converts wrt each dimension (ex: 1024x512)
    """
    if alpha:
        bands = im.split()
        bands = [b.resize(get_po2_res(im), Image.BILINEAR) for b in bands]
        return Image.merge('RGBA', bands)
    width, height = im.size
    new_dimX = get_closest(width)
    new_dimY = get_closest(height)
    return im.resize((new_dimX, new_dimY))


# https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes

def checkColorMode(im):
    cmode = im.mode
    name = im.filename
    if not cmode == 'RGB' and not cmode == 'RGBA':
        print("Info: File {} from {} is not RGB/RGBA color mode".format(name, cmode))
        # im = im.convert('RGB')


def grabICCProfile(im, removeIccProfile=True):
    name = im.filename
    icc = im.info.get('icc_profile')
    if icc is not None and removeIccProfile:
        print("Warning: {} has icc data, will be removed".format(name))
        return None
    return icc


class Housekeep:
    def __init__(self, files, opt, dryrun=False, compression=9, removeIccProfile=True):
        """
        Driver code
        Compression ranges from 0 to 9, 0 = no compression and 9 is max,
        PIL's default is 6

        files = List of files (collected from runHousekeeper)
        opt = Optimize, if enabled will take a long time to finish
        dryrun = If true will only print files that will be affected
        """
        for file in files:
            try:
                im = Image.open(file)
                ft = im.format.upper()

                if ft == "JPEG" or ft == "JPG":  # JPGs dont have ICC profiles
                    if not checkpo2(im):
                        continue
                    if not dryrun:
                        po2(im, False).save(file, quality = 100, subsampling = 0)
                elif ft == "PNG":
                    if not dryrun:
                        po2(im).save(
                            file,
                            icc_profile = grabICCProfile(im, removeIccProfile = removeIccProfile),
                            compress_level = compression,
                            format = 'PNG',
                            optimize = bool(opt)
                        )
                else:
                    po2(im).save(file)
            except IOError:
                print("IO ERROR: Is file an image? -> ", file)
