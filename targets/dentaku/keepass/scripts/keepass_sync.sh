#!/bin/bash

while true; do
    inotifywait -qq -e close_write ~/documents/private/keepass.kdbx;
    scp ~/documents/private/keepass.kdbx osmc@cjuub.se:/home/osmc/;
done

