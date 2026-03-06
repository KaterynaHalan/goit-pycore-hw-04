import sys
from pathlib import Path
from colorama import Fore, Style

def print_directory(path: Path, level = 1) -> None:
    for item in path.iterdir():
        space = "   " * level

        if item.is_dir():
            print(f"{space}{Fore.BLUE}{item.name}/{Style.RESET_ALL}")
            print_directory(item, level + 1)
        else:
            print(f"{space}{Fore.GREEN}{item.name}{Style.RESET_ALL}")


def main():
    if len(sys.argv) < 2:
        print("Please provide a path to a directory")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print("Path does not exist")
        return

    if not path.is_dir():
        print("Path is not a directory")
        return

    print(f"{Fore.YELLOW}{path.name}/{Style.RESET_ALL}")
    print_directory(path)


if __name__ == "__main__":
    main()