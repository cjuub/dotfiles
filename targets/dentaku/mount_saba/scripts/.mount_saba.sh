#!/bin/bash
sshfs -p 40000 -o ServerAliveInterval=5,ServerAliveCountMax=1 cjuub@192.168.1.12:/mnt/hdd /mnt/saba/hdd
sshfs -p 40000 -o ServerAliveInterval=5,ServerAliveCountMax=1 cjuub@192.168.1.12:/mnt/hdd /mnt/saba/ssd
