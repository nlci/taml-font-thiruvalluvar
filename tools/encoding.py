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
single.unicodes = [0x1133B]

ring.name = 'u1133C'
ring.unicodes = [0x1133C]

double.name = 'u1133C.dotdbl'
double.unicodes = []

rings.unicodes = []

## Omega
if font.info.familyName == 'Auvaiyar':
    greek = font['uni03A9']
    greek.unicodes = [0x03A9]

## Cleanup
dots = ('u0BCD', 'u1CDD', 'u1CDE', 'u1CDF')
for dot in dots:
    glyph = font[dot]
    for contour in glyph.contours:
        # print(dot)
        # print(len(contour))
        if len(contour) <= 2:
            glyph.removeContour(contour)

# Save UFO
font.changed()
font.save()
font.close()
