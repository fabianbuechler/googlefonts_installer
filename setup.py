"""Buchklub WBS (web-order-system)."""
import os
import re

from setuptools import setup


# Get __version__ from googlefonts_installer.py.
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(
        here, 'googlefonts_installer.py'), encoding='utf8') as version:
    VERSION = re.search(
        r'^__version__ = [\'"]([^\'"]*)[\'"]',
        version.read(), re.MULTILINE).group(1)
# Long description from readme and changelog.
with open(os.path.join(here, 'README.rst'), encoding='utf8') as readme:
    README = readme.read()
with open(os.path.join(here, 'CHANGELOG.rst'), encoding='utf8') as changelog:
    CHANGELOG = changelog.read()


setup(
    name='googlefonts_installer',
    description='Google fonts installer utility.',
    long_description=README + '\n\n' + CHANGELOG,
    version=VERSION,
    url='https://github.com/fabianbuechler/googlefonts_installer',
    license='MIT',
    author='Fabian Büchler',
    author_email='fabian@buechler.io',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Fonts',
    ],
    entry_points={'console_scripts': [
        'googlefonts-installer=googlefonts_installer:main'
    ]},
    py_modules=['googlefonts_installer'],
    zip_safe=False,
)
