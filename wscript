# thiruvalluvar

# set folder names
out='results'
TESTDIR='tests'
STANDARDS='tests/reference'

# set meta-information
script='taml'
APPNAME='nlci-' + script
VERSION='0.271'
TTF_VERSION='0.271'
COPYRIGHT='Copyright (c) 2009-2015, NLCI (http://www.nlci.in/fonts/)'

DESC_SHORT='Tamil Unicode font with OT and Graphite support'
DESC_LONG='''
Pan Tamil font designed to support all the languages using the Tamil script.
'''
DESC_NAME='NLCI-' + script
DEBPKG='fonts-nlci-' + script

# set test parameters
TESTSTRING=u'\u0c15'

# set fonts to build
faces = ('ThiruValluvar', 'Auvaiyar', 'Vaigai')
styles = ('-R', '-B', '-I', '-BI')
stylesName = ('Regular', 'Bold', 'Italic', 'Bold Italic')

# set build parameters
fontbase = 'source/'
tag = script.upper()

# create('master.sfd', cmd("../tools/ffaddapstotaml ${SRC} ${TGT}", ["source/master_src.sfd"]))
for f in faces :
    for (s, sn) in zip(styles, stylesName):
        if f == 'ThiruValluvar':
            ot = f + s
        else:
            ot = 'additional_faces'
        font(target = process(tag + f + '-' + sn.replace(' ', '') + '.ttf',
                name(tag + ' ' + f, lang='en-US', subfamily=(sn))
                ),
            source = fontbase + f + s + '.sfd',
            # sfd_master = 'master.sfd',
            # opentype = internal(),
            # sfd_master = 'source/master_src.sfd',
            # opentype = fea(fontbase + 'master_src.fea', no_make = True),
            opentype = fea(fontbase + ot + '.fea', no_make = True),
            graphite = gdl(fontbase + f + s + '.gdl',
                master = fontbase + 'master.gdl',
                make_params = '-l last -p 1',
                params = '-d'
                ),
            #classes = fontbase + 'thiruvalluvar_classes.xml',
            ap = f + s + '.xml',
            version = TTF_VERSION,
            copyright = COPYRIGHT,
            license=ofl('ThiruValluvar', 'Auvaiyar', 'Vaigai', 'NLCI'),
            woff = woff(),
            script = 'taml',
            # extra_srcs = ['tools/ffaddapstotaml'],
            fret = fret(params = '-r')
        )
