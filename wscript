#!/usr/bin/python3
# this is a smith configuration file

# thiruvalluvar

# command line options
opts = preprocess_args(
    {'opt' : '-l'}, # build fonts from legacy for inclusion into final fonts
    {'opt' : '-s'},  # only build a single font
    {'opt' : '--alllangs'} # test all language variants
    )

import os2

# override the default folders
DOCDIR = ['documentation', 'web']

# set meta-information
script='taml'
APPNAME='nlci-' + script

DESC_SHORT='Tamil Unicode font with OT and Graphite support'
DESC_NAME='NLCI-' + script
DEBPKG='fonts-nlci-' + script
getufoinfo('source/ThiruValluvar-Regular.ufo')
# BUILDLABEL = 'beta1'

langinfo = {
    # 'xub' : 'BK', # Betta Kurumba
    'xuj' : 'JK',  # Jennu Kurumba
    'iru' : 'IRU',  # Irula
    'ctt' : 'CTT',  # Chetti
}

# Set up the FTML tests
ftmlTest('tools/ftml-smith.xsl')

# set fonts to build
faces = ('ThiruValluvar', 'Auvaiyar', 'Vaigai')
facesLegacy = ('THIR', 'AUVA', 'VAIG')
styles = ('-R', '-B', '-I', '-BI')
stylesName = ('Regular', 'Bold', 'Italic', 'Bold Italic')
stylesLegacy = ('', 'BD', 'I', 'BI')

if '-s' in opts:
    faces = (faces[0],)
    facesLegacy = (facesLegacy[0],)
    styles = (styles[0],)
    stylesName = (stylesName[0],)
    stylesLegacy = (stylesLegacy[0],)

# set build parameters
fontbase = 'source/'
archive = fontbase + 'archive/unhinted/'
generated = 'generated/'
tag = '' # script.upper()

panose = [2, 0, 0, 3]
codePageRange = [0, 29]
unicodeRange = [0, 1, 2, 3, 4, 5, 6, 7, 15, 20, 29, 31, 32, 33, 35, 38, 39, 40, 45, 57, 60, 62, 67, 69, 91]
hackos2 = os2.hackos2(panose, codePageRange, unicodeRange)

if '-l' in opts:
    for f, fLegacy in zip(faces, facesLegacy):
        for (s, sn, sLegacy) in zip(styles, stylesName, stylesLegacy):
            extra = '../' + archive + 'VAIG' + sLegacy + '.ttf'
            missing_face = fLegacy
            if missing_face == 'AUVA':
                missing_face = 'VAIG' # used to be THIR
            missing = '../' + archive + missing_face + sLegacy + '.ttf'
            font(target = process('ufo/' + f + '-' + sn.replace(' ', '') + '.ttf',
                    cmd(hackos2 + ' ${DEP} ${TGT}'),
                    name(f, lang='en-US', subfamily=(sn))
                    ),
                source = legacy(f + s + '.ttf',
                                source = archive + fLegacy + sLegacy + '.ttf',
                                xml = fontbase + 'thiruvalluvar_unicode.xml',
                                params = ' -f ' + extra + ' -f ' + missing,
                                noap = '')
                )

psfix = 'cp' if '-p' in opts else 'psfix'

if '-l' in opts:
    faces = list()
for f in faces:
    p = package(
        appname = APPNAME + '-' + f.lower(),
        version = VERSION,
        docdir = DOCDIR # 'documentation'
    )
    for (s, sn) in zip(styles, stylesName):
        snf = '-' + sn.replace(' ', '')
        fontfilename = tag + f + snf
        font(target = process(fontfilename + '.ttf',
                cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', [fontbase + f + snf + '.ufo']),
                name(tag + ' ' + f)
                ),
            source = fontbase + f + snf + '.ufo',
            opentype=fea(generated + f + snf + '.fea',
                master=fontbase + 'master.feax',
                make_params='-L last',
                params='',
                ),
            graphite = gdl(generated + f + snf + '.gdl',
                master = fontbase + 'master.gdl',
                make_params = '-l last -p 1',
                params =  '-e ' + f + snf + '_gdlerr.txt'
                ),
            #classes = fontbase + 'thiruvalluvar_classes.xml',
            ap = generated + f + snf + '.xml',
            version = VERSION,
            woff = woff('woff/' + fontfilename + '.woff', params = '-v ' + VERSION + ' -m ../' + fontbase + f + '-WOFF-metadata.xml'),
            script = 'tml2', # taml
            package = p,
            pdf = fret(params = '-oi')
        )

        for langcode in langinfo.keys():
            langname = langinfo[langcode]
            langfontfilename = tag + f + langname.replace(' ', '') + snf
            n = font(target = process(langfontfilename + '.ttf',
                    cmd('psfdeflang -L ' + langcode + ' ${DEP} ${TGT}'),
                    name(tag + f + langname)
                    ),
                source = fontfilename + '.ttf',
                opentype = internal(),
                graphite = internal(),
                script = 'tml2',
                package = p,
                fret = fret(params = '-oi')
            )
            if '--alllangs' not in opts:
                n.no_test = True
