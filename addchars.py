#!/usr/bin/python3

from addcharslib import *

for f in faces:

    workshop = 1.4
    groman = 0.9
    croman = 0.8
    if f == 'ThiruValluvar':
        upm = 1.0
    else:
        upm = 1000.0/2048.0

    styles = {}
    if f == 'Vaigai':
        latin = 'charis'
        scale = str(croman*upm)
    else:
        latin = 'gentium'
        scale = str(groman*upm)
        if f == 'ThiruValluvar':
            styles['Bold'] = 'Medium'
            styles['Bold Italic'] = 'Medium Italic'
        else:
            styles['Regular'] = 'SemiBold'
            styles['Italic'] = 'SemiBold Italic'
            styles['Bold'] = 'ExtraBold'
            styles['Bold Italic'] = 'ExtraBold Italic'

    for sn in stylesName:
        modifyFile(scale, latin, f, sn, styles, chars='latn_import.txt')
