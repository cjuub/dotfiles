#!/usr/bin/env python3

from distutils.core import setup

setup(name='dotfiles_deployment',
      version='1.0',
      description='Deploys dotfiles to their specified locations',
      requires=['pyyaml'],
      entry_points={
            'console_scripts': [
                  'deploy_dotfiles = dotfiles_deployment.src.deploy:main'
            ]
      }
)
