#!/usr/bin/env python

import re
import setuptools

version = ""
with open('oson/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

with open("README.md", encoding='UTF-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="oson",
    version=version,
    author="woody",
    author_email="619434176@qq.com",
    description="This is a package for encode/decode python objects with json.",
    url="https://github.com/wuranxu/oson",
    install_requires=[],
    packages=setuptools.find_packages(exclude=("test")),
    python_requires='>=3.6',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=(
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3"
    ),
)
