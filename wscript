#!/usr/bin/python
# this is a smith configuration file

# thiruvalluvar

# command line options
opts = preprocess_args(
    {'opt' : '-l'}, # build fonts from legacy for inclusion into final fonts
    {'opt' : '-p'}, # do not run psfix on the final fonts
    {'opt' : '-s'}  # only build a single font
    )

import os2

# set the default output folders
out='results'

# locations of files needed for some tasks
DOCDIR = ['documentation', 'web']
STANDARDS='tests/reference'

# set meta-information
script='taml'
APPNAME='nlci-' + script
VERSION='0.271'
COPYRIGHT='Copyright (c) 2009-2018, NLCI (http://www.nlci.in/fonts/)'

DESC_SHORT='Tamil Unicode font with OT and Graphite support'
DESC_LONG='''
Pan Tamil font designed to support all the languages using the Tamil script.
'''
DESC_NAME='NLCI-' + script
DEBPKG='fonts-nlci-' + script

# set test parameters
TESTSTRING=u'\u0c15'
# ftmlTest('tools/FTMLcreateList.xsl')

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
generated = 'generated/'
tag = script.upper()

panose = [2, 0, 0, 3]
codePageRange = [0]
unicodeRange = [0, 1, 15, 20, 31, 45, 57]
hackos2 = os2.hackos2(panose, codePageRange, unicodeRange)

if '-l' in opts:
    for f, fLegacy in zip(faces, facesLegacy):
        for (s, sn, sLegacy) in zip(styles, stylesName, stylesLegacy):
            gentium = '../../../../latn/fonts/gentium_local/basic/1.102/zip/GenBkBas' + s.replace('-', '') + '.ttf'
            font(target = process(f + '-' + sn.replace(' ', '') + '.ttf',
                    cmd('cp ${DEP} ${TGT}'),
                    ),
                source = legacy(f + s + '.ttf',
                                source = fontbase + 'archive/' + fLegacy + sLegacy + '.ttf',
                                xml = fontbase + 'thiruvalluvar_unicode.xml',
                                params = '-f ' + gentium,
                                noap = '')
                )

psfix = 'cp' if '-p' in opts else 'psfix'

# create('master.sfd', cmd("../tools/ffaddapstotaml ${SRC} ${TGT}", ["source/master_src.sfd"]))
for f in faces:
#    p = package(
#        appname = APPNAME + '-' + f.lower(),
#        version = VERSION,
#        outdir = 'packages',
#        zipdir = ''
#    )
    for (s, sn) in zip(styles, stylesName):
        fontfilename = tag + f + '-' + sn.replace(' ', '')
        if f == 'ThiruValluvar':
            ot = f + s
        else:
            ot = 'additional_faces'
        font(target = process(fontfilename + '.ttf',
                cmd(hackos2 + ' ${DEP} ${TGT}'),
                name(tag + ' ' + f, lang='en-US', subfamily=(sn))
                ),
            source = fontbase + f + s + '.sfd',
            # sfd_master = 'master.sfd',
            # opentype = internal(),
            # sfd_master = 'source/master_src.sfd',
            # opentype = fea(fontbase + 'master_src.fea', no_make = True),
            opentype = fea(fontbase + ot + '.fea', no_make = True),
            graphite = gdl(generated + f + s + '.gdl',
                master = fontbase + 'master.gdl',
                make_params = '-l last -p 1',
                params = '-d'
                ),
            #classes = fontbase + 'thiruvalluvar_classes.xml',
            ap = generated + f + s + '.xml',
            version = VERSION,
            copyright = COPYRIGHT,
            license=ofl('ThiruValluvar', 'Auvaiyar', 'Vaigai', 'NLCI'),
            woff = woff('web/' + fontfilename + '.woff', params = '-v ' + VERSION + ' -m ../' + fontbase + f + '-WOFF-metadata.xml'),
            script = 'taml',
            # extra_srcs = ['tools/ffaddapstotaml'],
            # package = p,
            fret = fret(params = '')
        )
