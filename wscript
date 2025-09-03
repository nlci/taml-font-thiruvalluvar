#!/usr/bin/python3
# this is a smith configuration file

# thiruvalluvar

# command line options
opts = preprocess_args(
    {'opt' : '-l'}, # build fonts from legacy for inclusion into final fonts
    {'opt' : '-r'}, # only build the main regular font
    {'opt' : '-s'}, # only build the main font family
    {'opt' : '-t'}, # only build un-tuned fonts
    {'opt' : '--alllangs'} # test all language variants
    )

import os2

# override the default folders
DOCDIR = ['documentation', 'web']

# set meta-information
prefix = 'nlci-taml-'
APPNAME = prefix + 'thiruvalluvar'

DESC_SHORT='Tamil Unicode font with OT and Graphite support'
getufoinfo('source/ThiruValluvar-Regular.ufo')
# BUILDLABEL = 'beta1'

langinfo = {
    # 'xub' : 'BK', # Betta Kurumba
    # 'xuj' : 'JK',  # Jennu Kurumba
    'iru' : 'IRU',  # Irula
    'ctt' : 'CTT',  # Chetti
    # 'bad' : 'BDG',  # Badaga
}

line_spacing_info = {
    'ThiruValluvar': (-1244, 2152),
    'Auvaiyar': (-672, 1013),
    'Vaigai': (-609, 1045),
}

def set_line_spacing(langcode, fontname):
    cmd = 'cp'
    if langcode == 'iru':
        line_spacing = line_spacing_info[fontname]
        descender, ascender = line_spacing
        cmd = f'ttfascent -a {ascender} -d {-descender}'
    return cmd

# Set up the FTML tests
ftmlTest('tools/ftml-smith.xsl')

# set fonts to build
faces = ('ThiruValluvar', 'Auvaiyar', 'Vaigai')
facesLegacy = ('THIR', 'AUVA', 'VAIG')
styles = ('-R', '-B', '-I', '-BI')
stylesName = ('Regular', 'Bold', 'Italic', 'Bold Italic')
stylesLegacy = ('', 'BD', 'I', 'BI')
dspaces = ('Roman', 'Italic')

if '-s' in opts:
    faces = (faces[0],)

# set build parameters
fontbase = 'source/'
archive = fontbase + 'archive/unhinted/'
generated = 'generated/'

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

packages = {}
for f in faces:
    for langcode in langinfo.keys():
        if f != 'ThiruValluvar':
            familypackage = package(
                appname = prefix + f.lower(),
                version = VERSION,
                docdir = {'documentation': 'documentation', 'web_' + f.lower(): 'web'}
            )
            packages[f] = familypackage
        langpackage = package(
            appname = prefix + f.lower() + '-' + langcode,
            version = VERSION,
            docdir = ['documentation']
        )
        packages[f + langcode] = langpackage

cmds = [
    cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['${source}']),
    cmd('gftools fix-nonhinting -q --no-backup ${DEP} ${TGT}'),
    ]

for dspace in dspaces:
    d = designspace('source/' + 'ThiruValluvar' + dspace + '.designspace',
        target = process('${DS:FILENAME_BASE}.ttf', *cmds),
        instances = ['ThiruValluvar Regular'] if '-r' in opts else None,
        opentype=fea(generated + '${DS:FILENAME_BASE}.fea',
            mapfile = generated + '${DS:FILENAME_BASE}.map',
            master=fontbase + 'master.feax',
            make_params='-L last',
            params='',
            ),
        graphite = gdl(generated + '${DS:FILENAME_BASE}.gdl',
            master = fontbase + 'master.gdl',
            make_params = '-l last -p 1',
            params =  '-e ${DS:FILENAME_BASE}_gdlerr.txt'
            ),
        typetuner = typetuner('source/typetuner/feat_all.xml'),
        #classes = fontbase + 'thiruvalluvar_classes.xml',
        ap = generated + '${DS:FILENAME_BASE}.xml',
        version = VERSION,
        woff = woff('web/${DS:FILENAME_BASE}', type='woff2',
            metadata = '../source/${DS:FAMILYNAME_NOSPC}-WOFF-metadata.xml',
            dontship = True),
        script = 'tml2', # taml
        pdf = fret(params = '-oi')
    )

    for langcode in langinfo.keys():
        langname = langinfo[langcode]
        for fontfilename in d.fonts:
            (fontname, dash, remaining) = fontfilename.target.rpartition('-')
            langfontfilename = fontname + langname.replace(' ', '') + '-' + remaining
            n = font(target = process(langfontfilename,
                    # cmd('psfdeflang -L ' + langcode + ' ${DEP} ${TGT}'),
                    cmd('typetuner -o ${TGT} ' + f' applyset ../source/typetuner/feat_set_{langcode}.xml ' +  '${DEP}'),
                    cmd(set_line_spacing(langcode, fontname) + ' ${DEP} ${TGT}'),
                    name('ThiruValluvar' + langname)
                    ),
                source = fontfilename.target,
                opentype = internal(),
                graphite = internal(),
                script = 'tml2',
                package = packages['ThiruValluvar' + langcode],
                fret = fret(params = '-oi')
            )
            if '--alllangs' not in opts:
                n.no_test = True

for f in faces[1:]:
    for dspace in dspaces:
        d = designspace('source/' + f + dspace + '.designspace',
            target = process('${DS:FILENAME_BASE}.ttf', *cmds),
            opentype=fea(generated + '${DS:FILENAME_BASE}.fea',
                mapfile = generated + '${DS:FILENAME_BASE}.map',
                master=fontbase + 'master.feax',
                make_params='-L last',
                params='',
                ),
            graphite = gdl(generated + '${DS:FILENAME_BASE}.gdl',
                master = fontbase + 'master.gdl',
                make_params = '-l last -p 1',
                params =  '-e ${DS:FILENAME_BASE}_gdlerr.txt'
                ),
            typetuner = typetuner('source/typetuner/feat_all.xml'),
            ap = generated + '${DS:FILENAME_BASE}.xml',
            version = VERSION,
            woff = woff('web_' + f.lower() + '/${DS:FILENAME_BASE}', type='woff2',
                metadata = '../source/${DS:FAMILYNAME_NOSPC}-WOFF-metadata.xml',
                dontship = True),
            script = 'tml2',
            package = packages[f],
            pdf = fret(params = '-oi')
        )
        if '-t' in opts:
            continue

        for langcode in langinfo.keys():
            langname = langinfo[langcode]
            for fontfilename in d.fonts:
                (fontname, dash, remaining) = fontfilename.target.rpartition('-')
                langfontfilename = fontname + langname.replace(' ', '') + '-' + remaining
                n = font(target = process(langfontfilename,
                        cmd('typetuner -o ${TGT} ' + f' applyset ../source/typetuner/feat_set_{langcode}.xml ' +  '${DEP}'),
                        cmd(set_line_spacing(langcode, fontname) + ' ${DEP} ${TGT}'),
                        name(f + langname)
                        ),
                    source = fontfilename.target,
                    opentype = internal(),
                    graphite = internal(),
                    script = 'tml2',
                    package = packages[f + langcode],
                    fret = fret(params = '-oi')
                )
                if '--alllangs' not in opts:
                    n.no_test = True
