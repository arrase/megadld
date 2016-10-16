# MEGADLD
megadld is a demon for download public links from http://mega.co.nz.

Written for my download server, build on [Raspberry Pi](https://www.raspberrypi.org/)

### Dependencies
megatools is needed , the actual state of oficial [Meganz api](https://github.com/meganz/sdk) don't 
allows downloading public links , there is a [pull request](https://github.com/meganz/sdk/pull/397) but is 
not merged yet and the Python bindings are not finished.

You can find megatools at:

- https://megatools.megous.com/

- [megatools at GitHub](https://github.com/megous/megatools)

### Install
Run as root:
```
python setup.py install
```

### Configure
Edit as root:
```
vim /etc/megadld.conf
```

### Run from cmd
Run as root:
```
megadld start
```

### Start on boot
Run as root:
```
update-rc.d megadld defaults
```

### Troubleshooting
The error messages are written to syslog.

For the moment sending an invalid or malformed Mega url does not raise any error

### Available clients

- [Python client](https://github.com/arrase/megadld-cli)
- [Android client](https://github.com/arrase/megadld-cli-android)
