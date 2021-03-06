# telegram-bot
This telegram bot is useful to receive informations via Telegram messages about the [*InstaPy*](https://github.com/timgrossmann/InstaPy) script automated with cron.
This idea comes from this [*Telegram-bot*](https://github.com/Tkd-Alex/Telegram-InstaPy-Scheduling/) which allows to send commands to the bot.

### What you need
- Install [*python-telegram-bot*](https://github.com/python-telegram-bot/python-telegram-bot)
- InstaPy working on your pc/server.
- Telegram bot token.

### How to setup
1. Copy the needed files in your InstaPy folder (*telegram-bot-data*, *telegram_util.py* and *quickstart_telegram*).
2. Create a bot with [@BotFather](https://telegram.me/BotFather).
3. Populate *config.ini* with your data.
```
[telegram]
token = token_from_botfather without any ' or "
```
4. Contact [@GiveChatId_Bot](https://telegram.me/GiveChatId_Bot) and get your chat id with */chatid* command
5. Write your chat ID inside *allowed-id.txt*, one line for each allowed ID.
6. Insert your InstaPy script code inside the *try* block in the *run* function.
```python
def run():
    # Telegram bot setup

    try:

        # your instapy code goes here

    except:

        # error handling

    finally:

        # instapy session closing
```
7. Launch *quickstart_telegram.py* or put the bot functions inside your InstaPy script file.

### Bot functions
- *setup* is used to read the bot token, allowed IDs and start the Bot
- *sendStartJob* sends a message containing the name of the job and the starting time
- *sendEndJob* sends a message containing the name of the job and the ending time; It also sends an additional message containing the last 5 rows of the InstaPy *general.log* file. An example is:
```
Liked: 65
Already Liked: 0
Inappropriate: 25
Commented: 23
Followed: 9
```
- *sendError* sends a message containing the error traceback and the current time
