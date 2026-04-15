---
title: NLCI Tamil - Frequently Asked Questions
fontversion: 0.901
---

### *Why does the nukta not work in Microsoft Word?*

The nukta (either U+1133B or U+1133C) does not work in all cases with Microsoft DirectWrite,
which is what is used for text shaping in Microsoft Word (and other Microsoft applications),
as well as Windows itself.

See https://github.com/MicrosoftDocs/typography-issues/issues/738 for more details.

### *Why does the nukta not work in Adobe InDesign?*

First, you need to have HarfBuzz enabled as the text shaper.
Even with HarfBuzz enabled you might need to force the text to be redrawn.
See [Using SIL Fonts with Adobe InDesign](https://software.sil.org/fonts/indesign) for details.

Second, you need InDesign 2022 or later with U+1133B (but not U+1133C).
Adobe fixed one issue that allowed U+1133B to work,
but U+1133C does not work with InDesign.
See [Adobe User Voice](https://indesign.uservoice.com/forums/601180-adobe-indesign-bugs/suggestions/43164897-indesign-does-not-handle-a-nukta-with-tamil-script)
for more details and to up vote it if this issue is important to you.
If the source text you are working with uses U+1133C,
convert that character (in the copy of the text that has been imported into InDesign) to U+1133B.
Keep using U+1133C in the source text.

### *Which codepoint should I use?*

Ideally, you should use U+1133B for the single ring and the single dot,
and use U+1133C for the double ring and double dot.
However, as seen with the issue with InDesign above, not all applications will support this guideance.
