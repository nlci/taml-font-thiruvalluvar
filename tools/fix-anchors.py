#!/usr/bin/python3

from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# Modify UFO
above_marks = ('udatta', 'gravedeva', 'acutedeva', 'vedictonedoublesvarita', 'vedictonekathakaanudatta', 'candrabindugran')
below_marks = ('anudatta', 'vedictonedotbelow', 'vedictonetwodotsbelow', 'vedictonethreedotsbelow')
for glyph_name in above_marks + below_marks:
    glyph = font[glyph_name]
    (xmin, ymin, xmax, ymax) = glyph.bounds
    xcenter = (xmin + xmax) / 2
    glyph.width = 0
    if glyph.name in above_marks:
        glyph.appendAnchor('_V', (xcenter, ymin))
    if glyph.name in below_marks:
        glyph.appendAnchor('_N', (xcenter, 0))

virama = font['virama']
(xmin, ymin, xmax, ymax) = virama.bounds
for anchor in virama.anchors:
    if anchor.name == '_V':
        higher = ymin - anchor.y

for glyphname in ('virama', 'dotabovecomb', 'anusvara'):
    glyph = font[glyphname]
    for anchor in glyph.anchors:
        if anchor.name == '_V':
            anchor.y = ymin

for glyph in font:
    for anchor in glyph.anchors:
        if anchor.name == 'V' or anchor.name == '_V' and glyph.name in ('caroncomb', 'almostequaltocomb'):
            anchor.y += higher

# Save UFO
font.changed()
font.save()
font.close()
