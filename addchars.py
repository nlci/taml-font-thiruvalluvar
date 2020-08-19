#!/usr/bin/python3

from addcharslib import *

for f in faces:

    workshop = 1.4
    roman = 0.9
    if f == 'ThiruValluvar':
        upm2048 = 1.0
        upm1000 = 2048.0/1000.0
    else:
        upm2048 = 1000.0/2048.0
        upm1000 = 1.0
    scale2048 = str(upm2048*roman)
    scale1000 = str(upm1000*roman)

    if f == 'Auvaiyar':
        latin = 'charis'
    else:
        latin = 'gentium'

    for sn in stylesName:
        modifyFile(scale2048, latin, f, sn, chars = 'latn_import.txt')
        modifyFile(scale1000, 'runic', f, sn, lsn = 'Regular', chars = 'runr_import.txt')
