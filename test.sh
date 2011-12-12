#!/bin/sh
pythonloc=/mnt/us/launchpad/python/bin/python2.6
pythontest=/mnt/us/SotongDJ/python.py
pythonresult=/mnt/us/pytestres.txt
nowdate=`date +%d%m%Y`
test=`cat /mnt/us/SotongDJ/test`

case "$1" in
    python)
        $pythonloc $pythontest > $pythonresult
        ;;
    shell)
        ## Place the commands you prefer to run
        echo "YES!">$test/001-a-success.txt
        $pythonloc $pythontest
        ;;
esac

exit 0
