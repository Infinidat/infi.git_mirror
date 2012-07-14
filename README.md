Overview
========

A simple console script for mirroring git repositories between two remotes.

Usage
-----

```sh
easy_install infi.git_mirror
mirror_git_repository git://gitserver/some-repo.git git@github.com:Infinidat/some-repo.git
```

Checking out the code
=====================

This project uses buildout, and git to generate setup.py and __version__.py.
In order to generate these, run:

    python -S bootstrap.py -d -t
    bin/buildout -c buildout-version.cfg
    python setup.py develop

In our development environment, we use isolated python builds, by running the following instead of the last command:

    bin/buildout install development-scripts

