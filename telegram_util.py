#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telegram, os, time, traceback
from configparser import SafeConfigParser

class Telegram_Util:
    def __init__(self):
        self.allowed_id = []
        self.telegram_token = []
        self.bot = None

    def setup(self):
        # Create folder
        if not os.path.exists("telegram-bot-data"):
            os.makedirs("telegram-bot-data")

        # Load config
        config = SafeConfigParser()
        config.read('telegram-bot-data/config.ini')

        # Set telegram token
        self.telegram_token = config.get('telegram', 'token')

        # Get allowed IDs
        allowed_id = []
        with open('telegram-bot-data/allowed-id.txt') as f:
            for line in f:
                allowed_id.append(line.strip("\n"))

        # Set allowed IDs
        self.allowed_id = allowed_id

        # Create bot
        self.bot = telegram.Bot(self.telegram_token)


    def sendStartJob(self, job = 'InstaPy script'):
        # Sends the message to every allowed chat ID
        for chat_id in self.allowed_id:
            try:
                # Send message containing job and start time
                self.bot.send_message(chat_id, text='{} started at {}'.format(job, time.strftime("%X")))
            except:
                print(traceback.format_exc())

    def sendEndJob(self, job = 'InstaPy script'):
        # Sends the message to every allowed chat ID
        for chat_id in self.allowed_id:
            try:

                # Send message containing job and end time
                self.bot.send_message(chat_id, text='{} ended at {}'.format(job, time.strftime("%X")))

                # Read the last 5 line to get ended status of InstaPy.
                with open('logs/general.log', "r") as f:
                    f.seek (0, 2)                   # Seek @ EOF
                    fsize = f.tell()                # Get Size
                    f.seek (max (fsize-1024, 0), 0) # Set pos @ last n chars
                    lines = f.readlines()           # Read to end

                    lines = lines[-5:]              # Get last 5 lines
                    message = ''.join(str(x.replace("INFO - ", "")) for x in lines)
                # Send message containing InstaPy log
                self.bot.send_message(chat_id, text=message)
            except:
                print(traceback.format_exc())

    def sendError(self, error = 'some error occured'):
        # Sends the message to every allowed chat ID
        for chat_id in self.allowed_id:
            try:
                # Send message containing error info and error time
                self.bot.send_message(chat_id, text='Bot ended at {} because {}'.format(time.strftime("%X"), error))
            except:
                print(traceback.format_exc())
