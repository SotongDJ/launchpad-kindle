#!/bin/sh
python ./gitcho.py --action=checkout --mode=ifnot --target=master
git merge testing
git push origin master
git checkout testing
