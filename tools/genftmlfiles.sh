#!/bin/bash

# This script rebuilds the algorithmically-generated ftml files.

set -e

if [ ! -f wscript ]
then
	echo "Must be in the root of the project"
	exit 2
fi

# configure tests
tests="AllChars Diac Nuktas $1"
urls='url(../references/ThiruValluvar-Regular.ttf)=Ref url(../results/ThiruValluvar-Regular.ttf)=Gr url(../results/tests/ftml/fonts/ThiruValluvar-Regular_ot_tml2.ttf)=OT url(../results/ThiruValluvar-Bold.ttf)=Bold'
langs='ctt,iru,xub,xuj'
ufo='source/ThiruValluvar-Regular.ufo'

# list all the fonts to test
fonts=''
for url in $urls
do
	fonts="$fonts -s '$url'"
done

echo "Rebuilding ftml files..."
for test in $tests
do
	base=${test,,}
	title="\"${test} auto\""
	ftml=tests/${base}.ftml
	log=tests/logs/${base}.log
	eval tools/psfgenftml.py -q -t "$title" --langs $langs --scale 200 -i source/glyph_data-ThiruValluvar.csv --xsl ../tools/ftml.xsl "$fonts" -l $log $ufo $ftml &
done
wait
echo "done."
