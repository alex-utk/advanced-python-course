import click
import sys
from typing import Generator
from nl import file_reader


def get_stats(lines: Generator | list) -> tuple[int, int, int]:
    """Count stats

    Args:
        lines (Generator | list): lines source

    Returns:
        tuple[int, int, int]: number of lines, words, bytes
    """
    n_lines = 0
    n_words = 0
    n_bytes = 0

    for line in lines:
        n_lines += 1
        n_words += len(line.split())
        n_bytes += len(line.encode('utf-8'))

    return n_lines, n_words, n_bytes


@click.command()
@click.argument('file_pathes', nargs=-1, type=click.Path(exists=True))
def wc_func(file_pathes: tuple[str]) -> None:
    """Linux wc command copy

    Args:
        file_pathes (tuple[str]): list of pathes to files
    """
    if not file_pathes:
        lines = sys.stdin.readlines()
        n_lines, n_words, n_bytes = get_stats(lines)
        print(f'{n_lines}\t{n_words}\t{n_bytes}')
    else:
        n_lines_total = 0
        n_words_total = 0
        n_bytes_total = 0
        for file_path in file_pathes:
            lines = file_reader(file_path)
            n_lines, n_words, n_bytes = get_stats(lines)
            print(f'{n_lines}\t{n_words}\t{n_bytes}\t{file_path}')
            n_lines_total += n_lines
            n_words_total += n_words
            n_bytes_total += n_bytes

        if len(file_pathes) != 1:
            print(f'{n_lines_total}\t{n_words_total}\t{n_bytes_total}\tTOTAL')


if __name__ == '__main__':
    wc_func()
