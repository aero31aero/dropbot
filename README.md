# Dropbot

Simple Zulip bot to create digital ocean droplets.

## Running Instructions

1. Create a humanrc file which is the zuliprc of the human user account that's running the bot (used to fetch list of subscribers of the stream that are allowed to run the bot).
2. Create a dropletrc file which is the zuliprc of the bot user.
3. In the source code, change the line `stream='core team'` to the stream of your choice.
4. Create a `conf.ini` file like the `conf.ini-template`. Add your Digital Ocean API token there.
5. Install the dependencies from requirements.txt (`pip install -r requirements.txt`).
6. `zulip-run-bot dropbot.py -c dropletrc`. Preferably using supervisord or similar process manager.

At the end, you'll end up with a file structure like:

```
dropbot
├── conf.ini
├── conf.ini-template
├── create.py
├── dropbot.py
├── dropletrc
├── humanrc
```

You can modify the existing `run.sh` file for use with supervisord/cron.

## Contributing

[Zulip](https://github.com/zulip/zulip)'s CoC and contribution guidelines apply. The bot code is pretty rudimentary and the create.py file is copied from the Zulip server repo. We definitelhy need improvements in the code, but It Works<sup>TM</sup>.
