#!/bin/sh
python ./gitco.py master
git merge testing
git push origin master
git checkout testing
