#!/bin/bash

# This script rebuilds the algorithmically-generated ftml files.

# Copyright (c) 2020 SIL International  (http://www.sil.org)
# Released under the MIT License (http://opensource.org/licenses/

set -e

if [ ! -e OFL.txt ]
then
	echo "Please cd to root of font project to use this script"
	exit 2
fi

# configure tests
tests="AllChars Diac Nuktas $1"
urls='url(../references/ThiruValluvar-Regular.ttf)=Ref url(../results/ThiruValluvar-Regular.ttf)=Gr url(../results/tests/ftml/fonts/ThiruValluvar-Regular_ot_tml2.ttf)=OT url(../results/ThiruValluvar-Bold.ttf)=Bold'
langs='xub,xuj,iru,ctt'
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
	# base=$(basename $ftml .ftml)
	title="\"${test} auto\""
	ftml=tests/${test,,}.ftml
	log=tests/logs/${base}.log
	eval tools/psfgenftml.py -q -t "$title" $ufo $ftml --langs $langs --scale 200 -i source/glyph_data-ThiruValluvar.csv --xsl ../tools/ftml.xsl "$fonts" -l $log &
done
wait
echo "done."
