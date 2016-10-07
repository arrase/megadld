#!/bin/sh

### BEGIN INIT INFO
# Provides:        megadld
# Required-Start:  $network $remote_fs $syslog
# Required-Stop:   $network $remote_fs $syslog
# Default-Start:   2 3 4 5
# Default-Stop:    1
# Short-Description: Start Megadld daemon
### END INIT INFO

PATH=/sbin:/bin:/usr/sbin:/usr/bin

. /lib/lsb/init-functions

DAEMON=/usr/bin/megadld
PID=/var/run/megadld.pid

test -x $DAEMON || exit 5

case $1 in
	start)
		log_daemon_msg "Starting Megadld daemon" "Megadld"
		test -e $PID && log_daemon_msg "Megadld pid exist??" && rm $PID
		$DAEMON start
		log_end_msg $status
  		;;
	stop)
		log_daemon_msg "Stopping Megadld daemon" "Megadld"
		$DAEMON stop
		log_end_msg $?
  		;;
	restart)
		log_daemon_msg "Restart Megadld daemon" "Megadld"
		$DAEMON restart
  		;;
	*)
		echo "Usage: $0 {start|stop|restart}"
		exit 2
		;;
esac