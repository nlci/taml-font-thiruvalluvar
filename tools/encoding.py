#!/usr/bin/python3

from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# Modify UFO
single = font['u1133C']
double = font['u1133C.double']
ring = font['u1133C.ring']

single.name = 'u1133B.single'
single.unicode = None

ring.name = 'u1133B'
ring.unicode = 0x1133B

double.name = 'u1133C'
double.unicode = 0x1133C

# Save UFO
font.changed()
font.save()
font.close()
