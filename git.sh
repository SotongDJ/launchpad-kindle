#!/bin/sh
#~/github/launchpad-kindle/pull.sh
echo "Before continue, make sure the contents were pull down"
echo "from Kindle Keyboard before push to server and "
echo "the changelogs (include SCL) were added the desc. of the change."
read null
echo  Add change
rm -f ~/github/launchpad-kindle/*temp
rm -f ~/github/launchpad-kindle/*.pyc
rm -f ~/github/launchpad-kindle/*.conf
echo --------------------------------------------
echo Commit change
echo --------------------------------------------
echo Please enter the serial number:
read serial
echo 
echo Please enter your description of
echo this commit:
read commit
echo --------------------------------------------
#git commit -m "$commit"
git add -A
python ./gitcho.py --action=commit --date=`date +%d%m%Y` --serial=$serial --commit=$commit
echo ============================================
echo Push commit\(s\) to GitHub
python ./gitcho.py --action=push --mode=list --target=origin
echo ============================================
