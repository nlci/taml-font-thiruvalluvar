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
ring = font['nukta']
for anchor in ring.anchors:
    if anchor.name == '_N':
        if font.info.familyName == 'ThiruValluvar':
            anchor.y = -500
        else:
            anchor.y = -244
# ring.scaleBy(1.05)
ring.scaleBy(1.215)

## Move one nukta to the left
tti = font['tta_imatra']
for anchor in tti.anchors:
    if anchor.name == 'N':
        (xmin, ymin, xmax, ymax) = tti.bounds
        anchor.x = (xmax - xmin) * 0.35

## Position pulli over ku
ku = font['ka_umatra']
(xmin, ymin, xmax, ymax) = ku.bounds
for anchor in ku.anchors:
    if anchor.name == 'V':
        xcenter = (xmin + xmax) / 2
        anchor.x = xcenter

## Position nuktas with U and UU matras
sign_both = ['ja', 'ssa', 'sa', 'ha']
sign_u = ['nga', 'ca', 'pa', 'ya', 'va'] + sign_both
sign_U = ['ka'] + sign_both
nochange_u = [c + '_umatra' for c in sign_u]
nochange_U = [c + '_uumatra' for c in sign_U]
nochange = nochange_u + nochange_U
re_center = ['ka', 'nga', 'ca', 'pa', 'ma', 'ya', 'ra', 'lla', 'llla']

for glyph in font:
    nochange_u = []
    if glyph.name.endswith('_umatra') or glyph.name.endswith('_uumatra'):
        if glyph.name in nochange:
            continue
        (xmin, ymin, xmax, ymax) = glyph.bounds
        xcenter = (xmin + xmax) / 2
        for anchor in glyph.anchors:
            if anchor.name == 'N':
                anchor.y = ymin
                consonant_name = glyph.name.split('_')[0]
                if consonant_name in re_center:
                    anchor.x = xcenter

# Save UFO
font.changed()
font.save()
font.close()
