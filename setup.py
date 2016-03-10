"""Buchklub WBS (web-order-system)."""
import os

from setuptools import setup

# IMPORTANT: follow semantic versioning (SemVer) scheme described at semver.org!
VERSION = '0.3.0'


# Runtime requirements.
requires = []


# Long description from readme and changelog.
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as fp:
    README = fp.read()
with open(os.path.join(here, 'CHANGELOG.rst')) as fp:
    CHANGELOG = fp.read()


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
    install_requires=requires,
    include_package_data=True,
    packages=['.'],
    zip_safe=False,
)
