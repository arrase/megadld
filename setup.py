from distutils.core import setup

setup(
    # Application name:
    name="megadld",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Juan Ezquerro LLanes",
    author_email="arrase@gmail.com",

    # Packages
    packages=["megadld"],

    # Details
    url="https://github.com/arrase/megadld",

    description="megadld is a demon for download public links from http://mega.co.nz",

    data_files=[
        ('/etc/init.d', ['etc/init.d/megadld']),
        ('/etc/', ['etc/megadld.conf']),
        ('/usr/local/sbin', ['bin/megadld'])
    ]
)