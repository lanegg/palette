#!/usr/bin/env python3

from setuptools import setup


requires = [
    "PyYAML",
    "nose",
    "numpy",
    "opencv-contrib-python==3.4.7.28"
]

setup(
    name="palette",
    version="0.1",
    description="album player",
    author="lanegg",
    author_email="lanegg@sina.com",
    py_modules=['lib.mpv'],
    packages=[
        'core',
        ],
    # package_data={
    #     '': []
    #     },
    url="https://github.com/lanegg/palette",
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'start = core.palette'
        ]
    }
)