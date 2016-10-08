# MEGADLD
megadld is a demon for download public links from http://mega.co.nz.

Written for my download server, build on [Raspberry Pi](https://www.raspberrypi.org/)

### Dependencies
megatools is needed , the actual state of oficial [Meganz api](https://github.com/meganz/sdk) don't 
allows downloading public links , there is a [pull request](https://github.com/meganz/sdk/pull/397) but is 
not merged yet and the Python bindings are not finished, there are 
some [opened bug request](https://github.com/meganz/sdk/issues/435) for Python

You can find megatools at:

- https://megatools.megous.com/

- [megatools at GitHub](https://github.com/megous/megatools)

### ...where is the client??
State in progress...but you can do something like
```
echo '{"url":"<mega_url_with_key>"}'| nc <server_ip> 8000
```