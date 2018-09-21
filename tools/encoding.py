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

for g in (single, double, ring):
    if g.unicode:
        uni = f'{g.unicode:#x}'
    else:
        uni = 'un-encoded'
    print(f'before: name: {g.name} cp: {uni}')
    for unis in g.unicodes:
        print(f'cps: {unis:#x}')

single.name = 'u1133B'
single.unicode = 0x1133B
single.unicodes = [single.unicode]

ring.name = 'u1133C'
ring.unicode = 0x1133C
ring.unicodes = [ring.unicode]

double.unicodes = []

for g in (single, double, ring):
    if g.unicode:
        uni = f'{g.unicode:#x}'
    else:
        uni = 'un-encoded'
    print(f'after: name: {g.name} cp: {uni}')
    for unis in g.unicodes:
        print(f'cps: {unis:#x}')

# Save UFO
font.changed()
font.save()
font.close()
