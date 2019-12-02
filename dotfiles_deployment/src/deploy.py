import os
import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path
from shutil import copy2

import yaml


def main():
    if not os.getuid() == 0:
        subprocess.check_call(['sudo', sys.executable] + sys.argv)
        return

    parser = ArgumentParser()
    parser.add_argument('target', help='The target machine to deploy files for', type=str)
    args = parser.parse_args()

    target = args.target

    base_path = Path(__file__).absolute().parents[2]
    targets_yaml_path = base_path / 'targets.yaml'
    with targets_yaml_path.open() as fp:
        targets_data = yaml.safe_load(fp)

    if target not in targets_data.keys():
        raise Exception('Invalid target, valid choices are: ' + ', '.join(targets_data.keys()))

    target_deployments = targets_data[target]
    for deployment in target_deployments:
        deployment_yaml_path = base_path / 'targets' / target / deployment / 'deploy.yaml'
        with deployment_yaml_path.open() as fp:
            deployment_data = yaml.safe_load(fp)

        for entry in deployment_data['deploy']:
            src = base_path / 'targets' / target / deployment / entry['src']
            dst = entry['dst']

            copy2(src, dst)
            print(str(src) + ' -> ' + str(dst))


if __name__ == '__main__':
    main()
