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

single.name = 'nukta.dot'
single.unicode = None

ring.name = 'nukta'
ring.unicode = 0x1133C

double.name = 'nukta.dotdbl'
double.unicode = None

rings.unicode = None

# Save UFO
font.changed()
font.save()
font.close()
