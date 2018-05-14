import argparse
import zulip
import subprocess
import os

class HelloWorldHandler(object):
    def usage(self):
        return '''
        This is a boilerplate bot that responds to a user query with
        "beep boop", which is robot for "Hello World".

        This bot can be used as a template for other, more
        sophisticated, bots.
        '''

    def initialize(self, bot_handler):
        self.config_info = bot_handler.get_config_info('github_detail', optional=True)
        self.owner = self.config_info.get("owner", False)
        self.repo = self.config_info.get("repo", False)

        args = argparse.Namespace()

        args.cert_bundle=None
        args.client_cert=None
        args.client_cert_key=None
        args.insecure=False
        args.verbose=False
        args.zulip_api_key=None
        args.zulip_client=None
        args.zulip_config_file='/home/rohitt/Documents/temp/zulip/rohittrc'
        args.zulip_email=None
        args.zulip_site=None

        client = zulip.init_from_options(args)

        data = client.get_subscribers(stream='GCI mentors')
        # subscriptions =  client.get_subscribers(stream='GCI mentors')
        self.data = data
        print(data)

    def handle_message(self, message, bot_handler):
        length = len(self.data['subscribers'])
        if not message['sender_email'] in self.data['subscribers']:
            bot_handler.send_reply(message, "You are not allowed to use this bot.")
            return
        if message['content'] == 'help':
            bot_handler.send_reply(message, "Usage: `@mention <github-username>` to create a droplet.\n You can also pass other arguments of `tools/droplet/create.py` here.")
            message['content'] = '--help'
        else:
            bot_handler.send_reply(message, "Trying to create droplet. Please wait.")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        args = ['python', os.path.join(dir_path, 'create.py')]
        args = args + message['content'].split(' ')
        print(args)
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()
        outstring = out.decode("utf-8")
        successmsg = 'Instructions for use are below. (copy and paste to the user)'
        if successmsg in outstring:
            bot_handler.send_reply( message, outstring.split('------')[1])
        else:
            bot_handler.send_reply(message,  outstring)
            bot_handler.send_reply(message, err.decode("utf-8") )

handler_class = HelloWorldHandler
