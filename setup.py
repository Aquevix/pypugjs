#!/usr/bin/env python3


from distutils.core import setup

setup(
    name="pypugjs",
    version="0.1",
    description="Fork of original and deleted https://github.com/matannoam/pypugjs",
    author="Pavel Hrdina",
    packages=[
        "pypugjs",
        "pypugjs.ext",
        "pypugjs.ext.django",
        "pypugjs.ext.pyramid",
        "pypugjs.ext.tornado",
    ]
)
