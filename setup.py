#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='jack-matchmaker',
    version="1.0",
    description="Auto-connect new JACK ports.",
    #long_description='',
    author="Christopher Arndt",
    author_email="info@chrisarndt.de",
    url="https://github.com/SpotlightKid/jack-matchmaker",
    license="MIT License",
    packages=["jackmatchmaker"],
    entry_points={
        "console_scripts": [
            "jack-matchmaker = jackmatchmaker:main"
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        'Intended Audience :: End Users/Desktop',
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Sound/Audio :: MIDI",
    ]
)