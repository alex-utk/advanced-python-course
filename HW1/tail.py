import click
import sys


def file_reader_non_lazy(file_path: str) -> list[str]:
    """Non lazy filerader

    Args:
        file_path (str): path to file

    Yields:
        list[str]: list of strings
    """
    with open(file_path, "rt") as f:
        return f.read().splitlines()


def get_last_elements(lines, n):
    if n >= len(lines):
        return lines
    else:
        return lines[-n:]


@click.command()
@click.argument('file_pathes', nargs=-1, type=click.Path(exists=True))
def tail_func(file_pathes: tuple[str]) -> None:
    """Linux wc command copy

    Args:
        file_pathes (tuple[str]): list of pathes to files
    """
    if not file_pathes:
        lines = sys.stdin.readlines()
        lines = get_last_elements(lines, 17)
        print(f'==> stdin <==')
        for line in lines:
            print(line.rstrip())
    else:
        for file_path in file_pathes:
            if len(file_pathes) > 1:
                print(f'==> {file_path} <==')

            lines = file_reader_non_lazy(file_path)
            lines = get_last_elements(lines, 10)
            for line in lines:
                print(line.rstrip())


if __name__ == '__main__':
    tail_func()
