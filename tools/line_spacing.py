#!/usr/bin/python3

from ast import Pass
from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# Query UFO

## Find extra height (or depth) of line spacing needed with the extra vowels
extra_descender = extra_ascender = 0
for glyphname in ('CombCaron', 'almostequaltocomb', 'circumflexbelowcomb'):
    glyph = font[glyphname]
    (xmin, ymin, xmax, ymax) = glyph.bounds

    for anchor in glyph.anchors:
        if 'below' in glyphname:
            if anchor.name == '_N':
                extra = ymin - anchor.y
                extra_descender = min(extra_descender, extra)
        else:
            if anchor.name == '_V':
                extra = ymax - anchor.y
                extra_ascender = max(extra_ascender, extra)

## Find extra depth that the nukta adds
base_anchor = mark_anchor = 0
iru_nukta = font['nukta.ringdbl']
for anchor in iru_nukta.anchors:
    if anchor.name == 'N':
        base_anchor = anchor.y
    if anchor.name == '_N':
        mark_anchor = anchor.y
nukta_descender = base_anchor - mark_anchor

## Add extra height (or depth) to the base anchor points
descender = ascender = 0
for glyph in font:
    if glyph.name.startswith('nukta') or glyph.name in ('bindu', 'dotbelowcomb'):
        continue
    for anchor in glyph.anchors:
        if anchor.name == 'N':
            extra = anchor.y + extra_descender + nukta_descender
            descender = min(descender, extra)
        if anchor.name == 'V':
            extra = anchor.y + extra_ascender
            ascender = max(ascender, extra)

## Report on final values
print(f'{descender:5} {ascender:5}')
