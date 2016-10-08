import ConfigParser
import os.path
from sys import exit


class Config:
    _config_file = '/etc/megadld.conf'
    _log = None

    ip = None
    port = None
    download_dir = None
    megadl_path = None

    def __init__(self, log):
        self._log = log
        self._check_conf_file()
        self._load()
        self._check_conf_values()

    def _check_conf_file(self):
        if not os.path.isfile(self._config_file):
            self._log.error("File " + self._config_file + " does not exist")
            exit(2)

    def _load(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open(self._config_file))
        try:
            self.ip = config.get('network', 'ip')
            self.port = config.getint('network', 'port')
            self.download_dir = config.get('storage', 'download_dir')
            self.megadl_path = config.get('system', 'megadl_path')
        except ConfigParser.NoOptionError as e:
            self._log.error(e.message)
            exit(2)

    def _check_conf_values(self):
        if not os.path.isfile(self.megadl_path):
            self._log.error("File " + self.megadl_path + " does not exist")
            exit(2)

        if not os.path.isdir(self.download_dir):
            self._log.error("File " + self.download_dir + " does not exist")
            exit(2)
