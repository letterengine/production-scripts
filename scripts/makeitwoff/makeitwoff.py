'''This script converts .otf or .ttf fonts into .woff or .woff2'''

import os
from fontTools.ttLib import TTFont


def convert(fsDir: str, prFlvs: list, nwFlvs: list) -> None:
    '''This function transform your fonts from a previous flavor selected to a new one'''
    fsDir = fsDir.replace("'", '')
    try:
        for prFlv in prFlvs:
            fonts = [os.path.join(fsDir, f)
                     for f in os.listdir(fsDir) if prFlv in f]
            for f in fonts:
                font = TTFont(f)
                for nwFlv in nwFlvs:
                    font.flavor = nwFlv.replace('.', '')
                    font.save(f.replace(prFlv, nwFlv))
        print(f'Enjoy your {", ".join(nwFlvs)} fonts')
    except FileNotFoundError:
        print(f"Your selection didn't match the files in {fsDir}")


fontsDir = input('Please, copy or drag the path of your fonts!\n')
prevFlavors, newFlavors = ['.otf', '.ttf'], ['.woff', '.woff2']
pfi = int(input(
    'From which format do you want to convert (write the number)?\n1 - otf\n2 - ttf\n3 - both\n'))
nfi = int(input(
    'To which format do you want to convert (write the number)?\n1 - woff\n2 - woff2\n3 - both\n'))

# Flavors handle
prevFlavs = [prevFlavors[pfi-1]] if pfi != 3 else prevFlavors
newFlavs = [newFlavors[nfi-1]] if nfi != 3 else newFlavors
# Script run
convert(fontsDir, prevFlavs, newFlavs)
