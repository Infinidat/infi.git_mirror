from sys import argv, stdout

def mirror_git_repository(argv=argv[1:]):
    from logging import basicConfig, INFO
    from .. import mirror_git_repository as _func
    basicConfig(level=INFO, stream=stdout)
    from_url, to_url = argv
    _func(from_url, to_url)

