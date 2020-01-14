import os
import pwd
import subprocess
import yaml

from argparse import ArgumentParser
from pathlib import Path


def main():
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
            dst = Path(entry['dst'])

            os.makedirs(Path(dst).parent, exist_ok=True)
            copy_cmd = ['cp', str(src), str(dst)]
            user_home_path = str(pwd.getpwuid(os.getuid()).pw_dir)
            if not str(dst).startswith(user_home_path):
                subprocess.call(['sudo'] + copy_cmd)
            else:
                subprocess.call(copy_cmd)

            print(str(src) + ' -> ' + str(dst))


if __name__ == '__main__':
    main()
