#!/usr/bin/python3

from addcharslib import *

for f in faces:

    workshop = 1.4
    roman = 0.9
    if f == 'ThiruValluvar':
        upm = 1.0
    else:
        upm = 1000.0/2048.0
    scale = str(roman*upm)

    styles = {}
    if f == 'Auvaiyar':
        latin = 'charis'
    else:
        latin = 'gentium'
        styles = {
            'Regular': 'Medium',
            'Italic': 'Medium Italic',
            'Bold': 'ExtraBold',
            'Bold Italic': 'ExtraBold Italic'
        }

    for sn in stylesName:
        modifyFile(scale, latin, f, sn, styles, chars='latn_import.txt')
