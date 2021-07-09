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
single.unicode = 0x1133B

ring.name = 'nukta'
ring.unicode = 0x1133C

double.name = 'nukta.dotdbl'
double.unicode = None

rings.unicode = None

## Adjust new characters
anusvara = font['anusvara']
virama = font['virama']
anusvara.leftMargin = virama.leftMargin
anusvara.rightMargin = virama.rightMargin

# Save UFO
font.changed()
font.save()
font.close()
