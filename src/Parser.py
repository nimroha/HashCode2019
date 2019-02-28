import numpy as np


def parseIn(path):
    with open(path, 'r') as fp:
        numPhotos = int(fp.readline().strip().split()[0])
        photos    = []
        for line in fp:
            orientation, numTags, *tags = line.strip().split()
            photos.append({'orientation': orientation,
                           'numTags':     numTags,
                           'tags':        tags})

    return numPhotos, photos

def parseOut(path, slideshow):
    with open(path, 'w') as fp:
        fp.write(len(slideshow))
        [fp.write(slide) for slide in slideshow]
