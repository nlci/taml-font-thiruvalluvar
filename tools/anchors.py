#!/usr/bin/python3

from nameslist import *
from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)
print(f'Move anchors for {ufo}')

# Modify UFO


def ps_upm(points):
    """Covert a distance from a 2048 UPM font to a 1000 UPM font."""
    return int(points*1000/2048)


## Move single ring closer to base character
ring = font['nukta']
for anchor in ring.anchors:
    if anchor.name == '_N':
        closer = -500
        if font.info.familyName == 'ThiruValluvar':
            anchor.y = closer
        else:
            anchor.y = ps_upm(closer)
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

## Provide extra vowels
caroncomb = font['CombCaron']
caroncomb.unicode = 0x030C
(xmin, ymin, xmax, ymax) = caroncomb.bounds
xcenter = (xmin + xmax) / 2
caroncomb.appendAnchor('_U', (xcenter, ymin))

circumflexbelowcomb = font['CombCircumBlw']
(xmin, ymin, xmax, ymax) = circumflexbelowcomb.bounds
xcenter = (xmin + xmax) / 2
circumflexbelowcomb.appendAnchor('_L', (xcenter, ymax))

avagraha = font['uni16C7']
avagraha.name = 'avagraha'
avagraha.unicode = 0x1133D

## Posistion extra vowels on bases
offset = 250
if font.info.familyName != 'ThiruValluvar':
    offset = ps_upm(offset)

for glyph in font:
    for anchor in glyph.anchors:
        if anchor.name == 'V':
            glyph.appendAnchor('U', (anchor.x, anchor.y + offset))
        if anchor.name == 'N':
            glyph.appendAnchor('L', (anchor.x, anchor.y - offset))

# Save UFO
font.changed()
font.save()
font.close()
