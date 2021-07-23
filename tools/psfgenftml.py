#!/usr/bin/python3
'generate ftml tests from glyph_data.csv and UFO'
__url__ = 'http://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2018 SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Bob Hallissy'

from silfont.core import execute
import silfont.ftml_builder as FB

argspec = [
    ('ifont',{'help': 'Input UFO'}, {'type': 'infont'}),
    ('output',{'help': 'Output file ftml in XML format', 'nargs': '?'}, {'type': 'outfile', 'def': '_out.ftml'}),
    ('-i','--input',{'help': 'Glyph info csv file'}, {'type': 'incsv', 'def': 'glyph_data.csv'}),
    ('-f','--fontcode',{'help': 'letter to filter for glyph_data'},{}),
    ('-l','--log',{'help': 'Set log file name'}, {'type': 'outfile', 'def': '_ftml.log'}),
    ('--langs', {'help':'List of bcp47 language tags', 'default': None}, {}),
    ('--rtl', {'help': 'enable right-to-left features', 'action': 'store_true'}, {}),
    ('-t', '--test', {'help': 'which test to build', 'default': None, 'action': 'store'}, {}),
    ('-s','--fontsrc', {'help': 'font source: "url()" or "local()" optionally followed by "=label"', 'action': 'append'}, {}),
    ('--scale', {'help': '% to scale rendered text'}, {}),
    ('--ap', {'help': 'regular expression describing APs to examine', 'default': '.', 'action': 'store'}, {}),
    ('--xsl', {'help': 'XSL stylesheet to use'}, {}),

]


def doit(args):
    logger = args.logger

    # Read input csv
    builder = FB.FTMLBuilder(logger, incsv = args.input, fontcode = args.fontcode, font = args.ifont, langs=args.langs, ap = args.ap)

    # Override default base (25CC) for displaying combining marks:
    builder.diacBase = 0x0B95   # ka

    # Initialize FTML document:
    test = args.test or "AllChars (NG)"  # Default to "AllChars (NG)"

    # split labels from fontsource parameter
    fontsrc = []
    labels = []
    for sl in args.fontsrc:
        try:
            s, l = sl.split('=',1)
            fontsrc.append(s)
            labels.append(l)
        except ValueError:
            fontsrc.append(sl)
            labels.append(None)

    ftml = FB.FTML(test, logger, rendercheck = True, fontscale = args.scale, xslfn = args.xsl, fontsrc = fontsrc, fontlabel = labels)

    if test.lower().startswith("allchars"):
        # all chars that should be in the font:
        ftml.startTestGroup('Encoded characters')
        for uid in sorted(builder.uids()):
            if uid < 32: continue
            c = builder.char(uid)
            # iterate over all permutations of feature settings that might affect this character:
            for featlist in builder.permuteFeatures(uids = (uid,)):
                ftml.setFeatures(featlist)
                builder.render((uid,), ftml)
                # Don't close test -- collect consecutive encoded chars in a single row
            ftml.clearFeatures()
            for langID in sorted(c.langs):
                ftml.setLang(langID)
                builder.render((uid,), ftml)
            ftml.clearLang()

        # Add unencoded specials and ligatures -- i.e., things with a sequence of USVs in the glyph_data:
        ftml.startTestGroup('Specials & ligatures from glyph_data')
        for basename in sorted(builder.specials()):
            special = builder.special(basename)
            # iterate over all permutations of feature settings that might affect this special
            for featlist in builder.permuteFeatures(uids = special.uids):
                ftml.setFeatures(featlist)
                builder.render(special.uids, ftml)
                # close test so each special is on its own row:
                ftml.closeTest()
            ftml.clearFeatures()
            if len(special.langs):
                for langID in sorted(special.langs):
                    ftml.setLang(langID)
                    builder.render(special.uids, ftml)
                    ftml.closeTest()
                ftml.clearLang()

    if test.lower().startswith("diac"):
        # Diac attachment:

        # Representative base and diac chars:
        repDiac = filter(lambda x: x in builder.uids(), (0x0B82, 0x0BCD))
        repBase = filter(lambda x: x in builder.uids(), (0x0B95, 0x0B85))

        ftml.startTestGroup('Representative diacritics on all bases that take diacritics')
        for uid in sorted(builder.uids()):
            # ignore bases outside of the primary script:
            if uid < 0x0B80 or uid > 0x0BFF: continue
            c = builder.char(uid)
            # Always process Lo, but others only if that take marks:
            if c.general == 'Lo' or c.isBase:
                for diac in repDiac:
                    for featlist in builder.permuteFeatures(uids = (uid,diac)):
                        ftml.setFeatures(featlist)
                        # Don't automatically separate connecting or mirrored forms into separate lines:
                        builder.render((uid,diac), ftml, addBreaks = False)
                    ftml.clearFeatures()
                ftml.closeTest()

        ftml.startTestGroup('All diacritics on representative bases')
        for uid in sorted(builder.uids()):
            # ignore bases outside of the primary and Latin scripts:
            if uid < 0x0300 or uid in range(0xFE00, 0xFE10): continue
            c = builder.char(uid)
            if c.general == 'Mn':
                for base in repBase:
                    for featlist in builder.permuteFeatures(uids = (uid,base)):
                        ftml.setFeatures(featlist)
                        builder.render((base,uid), ftml, keyUID = uid, addBreaks = False)
                    ftml.clearFeatures()
                ftml.closeTest()

    if test.lower().startswith("nuktas"):
        # Nuktas:
        ftml.startTestGroup('Nuktas')
        test_name = test.lower().split()[0]
        with open(f'tests/{test_name}.template') as nuktas:
            line_number = 1
            for line in nuktas:
                for n in (0x0323, 0x1133B, 0x1133C):
                    for v in (0x0307, 0x0B82, 0x0BCD):
                        text = line.replace('N', chr(n))
                        text = text.replace('V', chr(v))
                        ftml.addToTest(None, text, label=f'line {line_number}', comment=f'n={n:04X} v={v:04X}')
                        ftml.closeTest()
                line_number += 1

    # Write the output ftml file
    ftml.writeFile(args.output)


def cmd() : execute("UFO",doit,argspec)
if __name__ == "__main__": cmd()
