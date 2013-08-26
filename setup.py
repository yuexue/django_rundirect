#!/usr/bin/env python

sdict = {
    'name': 'django_rundirect',
    'version': "0.1",
    'license': 'MIT',
    'packages': ['django_rundirect',
                 'django_rundirect.management',
                 'django_rundirect.management.commands'],
    'package_dir': {'django_rundirect': 'django_rundirect'}, 
    'zip_safe': False,
    'install_requires': ['django'],
    'author': 'Lichun',
    'url': 'https://gitcafe.com/yuexue/django_rundirect',
    'classifiers': [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python']
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**sdict)
