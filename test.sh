#!/bin/sh
pythonloc=/mnt/us/launchpad/python/bin/python2.6
pythontest=/mnt/us/launchpad/scripts/python.py
pythonresult=/mnt/us/pytestres.txt
nowdate=`date +%d%m%Y`

case "$1" in
    python)
		$pythonloc $pythontest > $pythonresult
        ;;
	shell)
		## Place the commands you prefer to run
		;;
esac

exit 0
