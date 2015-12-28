#!/usr/bin/env python3
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='ipip',
    version='0.1.0',
    description="A UI for PIP",
    long_description=readme,
    author="Andrew Popovych",
    author_email='piratus@gmail.com',
    url='https://github.com/piratus/ipip',
    packages=['ipip'],
    package_dir={'ipip': 'ipip'},
    include_package_data=True,
    install_requires=[
        'urwid==1.3.1'
    ],
    license="WTFPL",
    zip_safe=False,
    keywords='ipip',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: WTFPL License (WTFPL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    requires=['urwid'],
    scripts=['scripts/ipip']
)
