#!/mnt/us/python/bin/python2.6
import sys
sys.argv[1]

recentdate=`cat "$INSTALLDIR"/log`
		if [ "$nowdate" = "$recentdate" ]; then
			exit 0;
		fi
		cp "$WORKDIR"/money-temple.txt "$WORKDIR"/money-"$nowdate".txt
		echo "$nowdate" > "$INSTALLDIR"/log
        ;;
