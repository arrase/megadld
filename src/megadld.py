#!/usr/bin/python

import sys

from config_loader import Config
from daemonize import Daemonize
from log_writer import Logger

__application__ = "megadld"
__version__ = "0.1"
__release__ = __application__ + '/' + __version__
__author__ = "Juan Ezquerro LLanes"

if __name__ == "__main__":
    # Open logs
    log = Logger()
    # Load Config
    config = Config(log)
    # Load daemon
    daemon = Daemonize(log, config)

    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
