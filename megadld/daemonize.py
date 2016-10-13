import atexit
import os
import pwd
import sys
import time
from signal import SIGTERM

from server import Server


class Daemonize:
    _pidfile = '/var/run/megadld.pid'
    _stdin = '/dev/null'
    _stdout = '/dev/null'
    _stderr = '/dev/null'
    _log = None
    _config = None

    def __init__(self, log, config):
        self._log = log
        self._config = config

    def daemonize(self):
        """
        do the UNIX double-fork magic, see Stevens' "Advanced
        Programming in the UNIX Environment" for details (ISBN 0201563177)
        http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
        """
        try:
            pid = os.fork()
            if pid > 0:
                # exit first parent
                sys.exit(0)
        except OSError, e:
            self._log.error("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)

        # decouple from parent environment
        os.chdir("/")
        os.setsid()
        os.umask(0)

        # do second fork
        try:
            pid = os.fork()
            if pid > 0:
                # exit from second parent
                sys.exit(0)
        except OSError, e:
            self._log.error("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)

        # redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()
        si = file(self._stdin, 'r')
        so = file(self._stdout, 'a+')
        se = file(self._stderr, 'a+', 0)
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # write pidfile
        atexit.register(self.delpid)
        pid = str(os.getpid())
        file(self._pidfile, 'w+').write("%s\n" % pid)
        user = pwd.getpwnam(self._config.run_as)
        os.chown(self._pidfile, user[2], user[3])

        # close log at exit
        atexit.register(self._log.close())

        # Change process uid
        os.setuid(user[2])

    def delpid(self):
        os.remove(self._pidfile)

    def start(self):
        """
        Start the daemon
        """

        # Check for a pidfile to see if the daemon already runs
        try:
            pf = file(self._pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if pid:
            message = "pidfile %s already exist. Daemon already running?\n"
            self._log.error(message % self._pidfile)
            sys.exit(1)

        # Start the daemon
        self.daemonize()
        self.run()

    def stop(self):
        """
        Stop the daemon
        """
        # Get the pid from the pidfile
        try:
            pf = file(self._pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if not pid:
            message = "pidfile %s does not exist. Daemon not running?\n"
            self._log.error(message % self._pidfile)
            return  # not an error in a restart

        # Try killing the daemon process
        try:
            while 1:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
        except OSError, err:
            err = str(err)
            if err.find("No such process") > 0:
                if os.path.exists(self._pidfile):
                    os.remove(self._pidfile)
            else:
                print str(err)
                sys.exit(1)

    def restart(self):
        """
        Restart the daemon
        """
        self.stop()
        self.start()

    def run(self):
        # TODO: hacer server atributo para gestionar el stop y restart
        server = Server(self._log, self._config)
        server.run()
        for t in server.threads:
            t.join()
