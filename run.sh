#! /usr/bin/env bash
# simple script to be run by pm2 or other process manager
source ~/python-zulip-api/zulip-api-py3-venv/bin/activate
cd python-zulip-api/zulip_bots/zulip_bots
zulip-run-bot dropbot -c ../../dropletrc