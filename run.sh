#! /usr/bin/env bash
# simple script to be run by pm2 or other process manager
cd /home/rohitt
source python-zulip-api/zulip-api-py3-venv/bin/activate
zulip-run-bot clones/dropbot/dropbot.py -c clones/dropbot/dropletrc