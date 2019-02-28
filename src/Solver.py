import sys
import argparse
import os
import matplotlib.pyplot as plt

import numpy as np

INPUTS = {'a': '../inputs/a_example.txt',
          'b': '../inputs/b_lovely_landscapes.txt',
          'c': '../inputs/c_memorable_moments.txt',
          'd': '../inputs/d_pet_pictures.txt',
          'e': '../inputs/e_shiny_selfies.txt'}

from src.Parser import parseIn, parseOut

def plotHist(lst, title):
    max = np.max(lst)
    min = np.min(lst)
    plt.hist(lst, np.arange(start=min, stop=max))
    plt.title(title)
    plt.show()


def oneHotRun(photos):
    words = {}
    onehotSpace = 0
    for photo in photos:
        for tag in photo["tags"]:
            if tag not in words:
                words[tag] = {
                    "idx": onehotSpace,
                    "amount": 1
                }
                onehotSpace += 1
            else:
                words[tag]['amount'] += 1

    return words


def addOneHots2Photos(photos):
    words = oneHotRun(photos)
    for i in range(len(photos)):
        photos[i]["oneHot"] = np.zeros(len(words))
        for tag in photos[i]["tags"]:
            photos[i]["oneHot"][words[tag]["idx"]] += 1

    return words

def matchVerticals(photos):
    pass #TODO

def solveB(photos):
    pass #TODO

def main(argv=None):

    parser = argparse.ArgumentParser(description='Solve problem')

    parser.add_argument('--i', help='Path to input file.', required=True)

    args = parser.parse_args(argv)

    inPath  = INPUTS[args.i]
    outPath = os.path.splitext(inPath)[0] + '_result.txt'

    print("Parsing...")
    numPhotos, photos = parseIn(inPath)

    words = addOneHots2Photos(photos)
    print(len(words))
    print(words)
    wordOc = [w['amount'] for w in words.values()]
    plotHist(wordOc, 'Word occurences')
    # plotHist([p['numTags'] for p in photos], 'Number of tags per photo')

    photos.sort(key=lambda p: p['numTags'], reverse=True)

    verticals = [p for p in photos if p['orient'] == 'V']
    horizs    = [p for p in photos if p['orient'] == 'H']



    print("Solving...")
    # TODO

    # write solution to file
    print("Writing solution to file...")
    # TODO

    print("Done")


if __name__ == '__main__' :
    sys.exit(main())
