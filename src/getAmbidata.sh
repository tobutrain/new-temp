#!/bin/bash
SCREEN_NAME='getTemp'
SERVER_DIRECTORY='/var/www/html'
SERVER_FILE='/var/www/html/getAmbidata.py'

while true ; then
screen -S $SCREEN_NAME -X stuff 'python '$SERVER_FILE'\015'
sleep 30
fi