======================
Google Fonts Installer
======================

Installs selected fonts from the `Google fonts directory`_ by selectively
cloning the Git repository at `github.com/google/fonts`_ and creating symlinks
in your ``~/.fonts`` directory.

**Quickstart:**

..  code:: bash

    $ pipsi install googlefonts_installer
    $ mkdir -p ~/googlefonts
    $ cd ~/googlefonts
    $ vim googlefonts.conf
    $ googlefonts-installer

.. _Google fonts directory: https://www.google.com/fonts
.. _github.com/google/fonts: https://github.com/google/fonts

Requirements
============

To use this, you'll need

*   Python 3.4+ to run this script,
*   a recent version of Git supporting sparse checkouts,
*   a Linux-based system that uses the ``~/.fonts`` directory.

Usage
=====

#.  Create a directory for the Git clone:

    ..  code:: bash

        $ mkdir -p ~/Fonts/googlefonts/
        $ cd ~/Fonts/googlefonts/

#.  Install the ``googlefonts-installer`` package from PyPi. A good way to do
    this is via `pipsi`_:

    ..  code:: bash

        $ pipsi install googlefonts_installer

    You now have the ``googlefonts-installer`` command available.

#.  List the fonts to install, or more precicely the sub-paths of the Google
    fonts Git repository to clone, in a ``googlefonts.conf`` configuration file::

        ufl/ubuntu
        ofl/firamono
        ofl/firasans

#.  Run ``googlefonts-installer``. This …

    *   Sparse-clones (only the defined paths) the Google fonts Git repository
        (if not yet done).

    *   Pulls the latest changes.

    *   Creates symlinks for each font directory to ``~/.fonts``.

.. _pipsi: https://github.com/mitsuhiko/pipsi/

Defaults
--------

The ``googlefonts-installer`` command defaults to cloning into the current
working directory and symlinking to ``~/.fonts``, the ``googlefonts.conf``
configuration file is assumed to be in the current working directory as well.

Use the ``--work-dir``, ``--fonts-dir`` and ``--config`` arguments to overwrite
this.

Hint
----

To find the sub-paths of the fonts you'd like to install, go to
https://github.com/google/fonts, hit ``t`` and start typing a font's name.

Github will list all matching file names.
For example, to install *Ubuntu Regular*, use the directory part of the file
``ufl/ubuntu/Ubuntu-Regular.ttf`` listed by Github.
