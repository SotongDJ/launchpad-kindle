#!/bin/sh
~/github/launchpad-kindle/pull.sh
echo  Add change
git add -A
echo --------------------------------------------
echo Commit change
echo --------------------------------------------
echo Please enter your description of
echo this commit:
read commit
echo --------------------------------------------
git commit -m "$commit"
echo ============================================
echo Push commit\(s\) to GitHub
python ./gitcho.py nonch push origin
echo ============================================
