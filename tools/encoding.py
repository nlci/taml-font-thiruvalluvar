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

## Cleanup
vedic_dots = ('u1CDD', 'u1CDE', 'u1CDF')
for vedic_dot in vedic_dots:
    glyph = font[vedic_dot]
    for contour in glyph.contours:
        if len(contour) <= 2:
            glyph.removeContour(contour)

# Save UFO
font.changed()
font.save()
font.close()
