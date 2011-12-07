#!/bin/sh
if [ -d "/mnt/us/record" ]; then
  mkdir -p "/mnt/us/record"
fi
case "$1" in
    start)
		name=`date +%Y-%m-%d_%H-%M-%S`
        arecord -qN /mnt/us/record/$name.wav
        ;;
    end)
        kill -TERM `pidof arecord`
        ;;
    *)
        echo "Usage: $0 {start|end}"
        exit 1
        ;;
esac

exit 0