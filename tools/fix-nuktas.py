#!/usr/bin/python3

from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# Modify UFO
vedic = font['vedictonedotbelow']
(xmin, ymin, xmax, ymax) = vedic.bounds
vedic_beltline = (ymin + ymax) / 2

for glyph in font:
    if glyph.name.startswith('nukta'):
        (xmin, ymin, xmax, ymax) = glyph.bounds
        nukta_beltline = (ymin + ymax) / 2
        glyph.moveBy((0, vedic_beltline - nukta_beltline))

# Save UFO
font.changed()
font.save()
font.close()
