__import__("pkg_resources").declare_namespace(__name__)

from contextlib import contextmanager
from logging import getLogger

logger = getLogger()

@contextmanager
def chdir(path):
    import os
    current_directory = os.path.abspath(os.curdir)
    try:
        logger.info("chdir to {}".format(path))
        os.chdir(path)
        yield
    finally:
        logger.info("chdir back to {}".format(current_directory))
        chdir(current_directory)

@contextmanager
def with_tempdir():
    from shutil import rmtree
    from os import makedirs, path
    from tempfile import mkdtemp
    tempdir = mkdtemp()
    if not path.exists(tempdir):
        makedirs(tempdir)
    try:
        with chdir(tempdir):
            yield tempdir
    finally:
        rmtree(tempdir)

def mirror_git_repository(from_url, to_url):
    from infi.execute import execute_assert_success
    with with_tempdir():
        execute_assert_success(command=["git", "clone", "--bare", from_url, "clone"])
        with chdir("clone"):
            execute_assert_success(command=["git", "remote", "add", "github", to_url])
            execute_assert_success(command=["git", "push", "github", "--all"])
            execute_assert_success(command=["git", "push", "github", "--tags"])
