#!/bin/sh
git checkout master
git merge testing
git push origin master
git checkout testing
