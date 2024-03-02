import click
import sys
from typing import Generator

# https://sanjayasubedi.com.np/python/python-tips-lazy-evaluation-in-python/
# https://stackoverflow.com/a/49752733


def file_reader(file_path: str) -> Generator[str, None, None]:
    """Lazy filerader supporting big files

    Args:
        file_path (str): path to file

    Yields:
        Generator[str, None, None]: generator returning line by line
    """
    with open(file_path, "rt", encoding="utf-8") as f:
        for line in f:
            yield line


@click.command()
@click.argument('file_path', default=".", nargs=1, type=click.Path(exists=True))
def nl_func(file_path: str) -> None:
    """Linux nl command copy

    Args:
        file_path (str): path to file
    """
    if file_path == '.':
        lines = sys.stdin.readlines()
    else:
        lines = file_reader(file_path)

    for idx, line in enumerate(lines, start=1):
        print(f'{idx}\t{line.rstrip()}')


if __name__ == '__main__':
    nl_func()
