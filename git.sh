#!/bin/sh
#~/github/launchpad-kindle/pull.sh
echo "Before continue, make sure the contents were pull down"
echo "from Kindle Keyboard before push to server and "
echo "the changelogs (include SCL) were added the desc. of the change."
read null
echo  Add change
rm -f ~/github/launchpad-kindle/*temp
rm -f ~/github/launchpad-kindle/*.pyc
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
