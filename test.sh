#!/bin/sh
pythonloc=/mnt/us/python/bin/python
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
	sshver)
		echo ----------------------------------------------------------
		ps -A|grep sshd
		echo ----------------------------------------------------------
		netstat -nap|grep :22
		echo ----------------------------------------------------------
		service sshd restart
		echo ----------------------------------------------------------
		;;
esac

exit 0
