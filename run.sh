#! /usr/bin/env bash
# simple script to be run by pm2 or other process manager
cd "$(dirname "$0")"
source ./env/bin/activate
zulip-run-bot dropbot.py -c dropletrc
