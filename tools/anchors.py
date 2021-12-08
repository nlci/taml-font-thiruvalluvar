#!/usr/bin/python3

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


## Adjust new characters
anusvara = font['anusvara']
# vedictonedoublesvarita = font['vedictonedoublesvarita']
virama = font['virama']
anusvara.leftMargin = virama.leftMargin
anusvara.rightMargin = virama.rightMargin
(xmin, ymin, xmax, ymax) = anusvara.bounds
xcenter = (xmin + xmax) / 2
for anchor in virama.anchors:
    if anchor.name == '_V':
        x = xcenter
        y = anchor.y
        anusvara.appendAnchor('_V', (x, y))
        # vedictonedoublesvarita.appendAnchor('_V', (x, y))

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

## Provide extra vowels...
base_offset = 250
mark_offset = 20
if font.info.familyName != 'ThiruValluvar':
    base_offset = ps_upm(base_offset)
    mark_offset = ps_upm(mark_offset)

caroncomb = font['CombCaron']
caroncomb.unicode = 0x030C

ka = font['ka']
top = 0
for anchor in ka.anchors:
    if anchor.name == 'V':
        top = anchor.y

for glyphname in ('CombCaron', 'almostequaltocomb', 'circumflexbelowcomb', 'aamatra', 'aulengthmark'):
    glyph = font[glyphname]
    (xmin, ymin, xmax, ymax) = glyph.bounds
    xcenter = (xmin + xmax) / 2
    if 'below' in glyphname:
        glyph.appendAnchor('_N', (xcenter, ymax + base_offset))
    elif 'ma' in glyphname:
        # ...even on bases that do not normally take a virama (on V)
        glyph.appendAnchor('V', (xcenter, top))
    else:
        glyph.appendAnchor('_V', (xcenter, ymin - base_offset))
        glyph.appendAnchor('V', (xcenter, ymax - base_offset))

## Posistion extra vowels on nuktas (U+1133C and related)

# anchor for nukta as a base
for glyph in font:
    if glyph.name.startswith('nukta'):
        (xmin, ymin, xmax, ymax) = glyph.bounds
        xcenter = (xmin + xmax) / 2
        glyph.appendAnchor('N', (xcenter, ymin - mark_offset + base_offset))

# get anchor posistion from nukta glyph...
(xmin, ymin, xmax, ymax) = ring.bounds
for anchor in ring.anchors:
    if anchor.name == '_N':
        xmark = anchor.x
        ymark = anchor.y
    if anchor.name == 'N':
        xbase = anchor.x
        ybase = anchor.y

# ...to apply to the composite nuktas
for glyph in font:
    if glyph.name in ('bindu', 'dotbelowcomb'):  # 'vedictonekathakaanudatta', 'vedictonedotbelow', 'vedictonetwodotsbelow', 'vedictonethreedotsbelow'
        glyph.appendAnchor('N', (xbase, ybase))
        for anchor in glyph.anchors:
            if anchor.name == '_N':
                anchor.x = xmark
                anchor.y = ymark

# Save UFO
font.changed()
font.save()
font.close()
