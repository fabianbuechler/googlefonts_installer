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
    # Add list of font paths from git repo to:
    $ vim googlefonts.conf
    $ googlefonts-installer

To **update fonts** from Git, **install new fonts** or **remove fonts**, just
(optionally) change ``googlefonts.conf`` and re-run ``googlefonts-installer``.

.. _Google fonts directory: https://www.google.com/fonts
.. _github.com/google/fonts: https://github.com/google/fonts

Requirements
============

To use this, you'll need

*   Python 3.3+ to run this script,
*   a recent version of Git supporting sparse checkouts,
*   a Linux-based system that uses the ``~/.fonts`` directory.

Usage / How it works
====================

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
    fonts Git repository to clone, in a ``googlefonts.conf`` configuration
    file, e.g.::

        ufl/ubuntu
        ofl/firamono
        ofl/firasans

    For example, to install *Ubuntu Regular*, use the directory part
    ``ufl/ubuntu/`` of the file ``ufl/ubuntu/Ubuntu-Regular.ttf`` in the
    repository.

#.  Run ``googlefonts-installer``. This …

    *   If not yet done, inits a Git repository with sparse-checkout
        (only clone the defined paths) and adds the Google fonts Git repository
        as a remote.

    *   Pulls the latest changes (shallow history to save space).

    *   Creates symlinks for each font directory to ``~/.fonts``.

    *   Removes broken symlinks from ``~/.fonts`` for uninstalled (removed from
        ``googlefonts.conf``) fonts.

.. _pipsi: https://github.com/mitsuhiko/pipsi/

Defaults
--------

The ``googlefonts-installer`` command defaults to:

*   reading config from ``googlefonts.conf`` in the current working directory,
*   cloning into the current working directory and
*   symlinking to ``~/.fonts``.

Use the ``--config``, ``--work-dir`` and ``--fonts-dir`` arguments to change
this behaviour.

Hint
----

To find the sub-paths of the fonts you'd like to install, go to
https://github.com/google/fonts, hit ``t`` and start typing a font's name.
Github will list all matching file names.
