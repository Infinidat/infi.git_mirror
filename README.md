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

This project uses buildout and infi-projector, and git to generate setup.py and __version__.py.
In order to generate these, first get infi-projector:

    easy_install infi.projector

    and then run in the project directory:

        projector devenv build
