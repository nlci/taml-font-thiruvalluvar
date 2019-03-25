#!/usr/bin/python3

from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# Modify UFO

## Nuktas
single = font['nukta']
double = font['nukta.double']
ring = font['nukta.ring']
rings = font['nukta.ringdbl']

single.name = 'nuktanew'
single.unicodes = [0x1133B]

ring.name = 'nukta'
ring.unicodes = [0x1133C]

double.name = 'nukta.dotdbl'
double.unicodes = []

rings.unicodes = []

## Omega
if font.info.familyName == 'Auvaiyar':
    greek = font['u03A9']
    greek.unicodes = [0x03A9]

## Cleanup
dots = ('virama', 'vedictonedotbelow', 'vedictonetwodotsbelow', 'vedictonethreedotsbelow')
for dot in dots:
    glyph = font[dot]
    for contour in glyph.contours:
        # print(dot)
        # print(len(contour))
        if len(contour) <= 2:
            glyph.removeContour(contour)

## Adjust new characters
anusvara = font['anusvara']
virama = font['virama']
anusvara.leftMargin = virama.leftMargin
anusvara.rightMargin = virama.rightMargin

# Save UFO
font.changed()
font.save()
font.close()
