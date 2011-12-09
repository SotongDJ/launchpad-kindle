#!/bin/sh
python ./gitcho.py change checkout master
git merge testing
git push origin master
git checkout testing
