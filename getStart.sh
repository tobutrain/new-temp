#!/bin/bash
SCREEN_NAME='getTemp'
SERVER_DIRECTORY='/var/www/html'
SERVER_FILE='/var/www/html/getAmbidata.py'

#screenが立ち上がっていなかったら立てる
if ! screen -ls | grep $SCREEN_NAME ; then
    screen -md $SCREEN_NAME
fi
screen -S $SCREEN_NAME -X stuff 'cd '$SERVER_DIRECTORY'\015'
screen -S $SCREEN_NAME -X stuff 'sh '$SERVER_DIRECTORY'/src/getAmbidata.sh\015'