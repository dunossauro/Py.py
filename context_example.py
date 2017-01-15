from contextlib import contextmanager
from os import getcwd, chdir, listdir


@contextmanager
def cd(path):
    prev_cwd = getcwd()
    chdir(path)
    try:
        yield
    finally:
        chdir(prev_cwd)

print(getcwd(), listdir()[0])
with cd('..'):
    print(getcwd(), listdir()[0])

print(getcwd(), listdir()[0])
