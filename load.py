#!/usr/bin/env python3

import os
import shutil

from argparse import ArgumentParser
from pathlib import Path
from typing import Dict


def merge_dotfiles(common_path: Path, target_path: Path) -> Dict[Path, str]:
    dotfiles = {}
    for file in common_path.glob('**/*'):
        if not file.is_file():
            continue

        dotfiles[file.relative_to(common_path)] = file.open().read()

    for file in target_path.glob('**/*'):
        if not file.is_file():
            continue

        dotfiles.setdefault(file.relative_to(target_path), '')
        dotfiles[file.relative_to(target_path)] += file.open().read()

    return dotfiles


def _is_ignored_file(file: Path):
    if 'zsh' in file.name and '/zsh' not in os.environ['SHELL']:
        return True

    if 'bash' in file.name and '/bash' not in os.environ['SHELL']:
        return True

    return False


def copy_dotfiles(dotfiles: Dict[Path, str]):
    for file, content in dotfiles.items():
        if _is_ignored_file(file):
            continue

        home_path = Path(os.environ['HOME'])
        dst = home_path / file
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(content)
        print(str(file) + ' --> ' + str(dst))


def main():
    parser = ArgumentParser()
    parser.add_argument('target')
    args = parser.parse_args()

    targets = ['desktop', 'dell_xps_15_9570']

    if args.target not in targets:
        print('Select a target: ' + str(targets))

    dotfiles = merge_dotfiles(Path('common'), Path(args.target))
    copy_dotfiles(dotfiles)


if __name__ == '__main__':
    main()
