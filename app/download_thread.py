import json
import subprocess
from threading import Thread


# Multithreaded Python server : TCP Server Socket Thread Pool
class DownloadThread(Thread):
    _conn = None
    _config = None

    def __init__(self, conn, config):
        Thread.__init__(self)
        self._config = config
        self._conn = conn

    def run(self):
        # Get data from client
        data = json.loads(self._conn.recv(2048))
        # Check valid json
        if not data.has_key("url"):
            self._conn.send('{"status":"false"}')
            self._conn.close()
            return False
        # Respond to user
        self._conn.send('{"status":"true"}')
        self._conn.close()
        # Start download
        subprocess.call(
            [self._config.megadl_path, "--no-progress", "--path=" + self._config.download_dir, data["url"]])