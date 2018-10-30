#!/usr/bin/python3

from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# Modify UFO

## Nuktas
single = font['u1133C']
double = font['u1133C.double']
ring = font['u1133C.ring']
rings = font['u1133C.ringdbl']

single.name = 'u1133B'
single.unicode = 0x1133B
single.unicodes = [single.unicode]

ring.name = 'u1133C'
ring.unicode = 0x1133C
ring.unicodes = [ring.unicode]

double.name = 'u1133C.dotdbl'
double.unicodes = []

rings.unicodes = []

## Omega
if font.info.familyName == 'Auvaiyar':
    greek = font['uni03A9']
    greek.unicode = 0x03A9
    greek.unicodes = [greek.unicode]

# Save UFO
font.changed()
font.save()
font.close()
