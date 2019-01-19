#!/usr/bin/python3

from nameslist import *
from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)
print(f'Move anchors for {ufo}')

# Modify UFO

## Move single ring closer to base character
ring = font['u1133C']
for anchor in ring.anchors:
    if anchor.name == '_N':
        if font.info.familyName == 'ThiruValluvar':
            anchor.y = -500
        else:
            anchor.y = -244

## Move one nukta to the left
tti = font['u0B9F_u0BBF']
for anchor in tti.anchors:
    if anchor.name == 'N':
        (xmin, ymin, xmax, ymax) = tti.bounds
        anchor.x = (xmax - xmin) * 0.35

## Position nuktas with U and UU matras
sign_both = ['0B9C', '0BB7', '0BB8', '0BB9']
sign_u = ['0B99', '0B9A', '0BAA', '0BAF', '0BB5'] + sign_both
sign_U = ['0B95'] + sign_both
nochange_u = ['u' + c + '_u0BC1' for c in sign_u]
nochange_U = ['u' + c + '_u0BC2' for c in sign_U]
nochange = nochange_u + nochange_U
re_center = ['0B95', '0B99', '0B9A', '0BAA', '0BAE', '0BAF', '0BB0', '0BB3', '0BB4']

for glyph in font:
    nochange_u = []
    if glyph.name.endswith('_u0BC1') or glyph.name.endswith('_u0BC2'):
        if glyph.name in nochange:
            continue
        (xmin, ymin, xmax, ymax) = glyph.bounds
        xcenter = (xmin + xmax) / 2
        for anchor in glyph.anchors:
            if anchor.name == 'N':
                anchor.y = ymin
                consonant_name = glyph.name.split('_')[0]
                consonant_name = consonant_name[1:] # remove initial u
                if consonant_name in re_center:
                    anchor.x = xcenter

# Save UFO
font.changed()
font.save()
font.close()
