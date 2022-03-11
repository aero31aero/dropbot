#! /usr/bin/env bash
# simple script to be run by pm2 or other process manager
source ./env/bin/activate
zulip-run-bot dropbot.py -c dropletrc
