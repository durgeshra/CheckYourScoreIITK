#!/bin/sh

export DISPLAY=:0
python3 checkMarks.py > updatedMarks.txt
old="prevMarks.txt"
new="updatedMarks.txt"

file1=`md5sum $old | awk '{ print $1 }'`
file2=`md5sum $new | awk '{ print $1 }'`

if [ "$file1" != "$file2" ]
then
notify-send "New Marks Added!"
cp updatedMarks.txt prevMarks.txt
fi

