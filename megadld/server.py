import socket
from sys import exit

from download_thread import DownloadThread


class Server():
    _log = None
    _config = None
    _tcpServer = None

    threads = []

    def __init__(self, log, config):
        self._log = log
        self._config = config

    def run(self):
        try:
            self._tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self._tcpServer.bind((self._config.ip, self._config.port))
        except socket.error:
            self._log.error("There was an error when trying to bind the server")
            exit(2)
        finally:
            self._log.info("Waiting for connections ...")

        while True:
            self._tcpServer.listen(4)
            (conn, (ip, port)) = self._tcpServer.accept()
            newthread = DownloadThread(conn, self._config)
            newthread.start()
            self.threads.append(newthread)
