#!/bin/bash

from instapy import InstaPy
import random
from telegram_util import Telegram_Util


def run():

    # Initialize telegram bot
    telegram_bot = Telegram_Util()
    telegram_bot.setup()

    try:
        insta_username = 'username'
        insta_password = 'password'

        session = InstaPy(username=insta_username,
                          password=insta_password,
                          headless_browser=False,
                          use_firefox=True,
                          nogui=True)
        session.login()

        random.seed()
        # settings
        session.set_upper_follower_count(limit=5000)
        session.set_lower_follower_count(limit=10)

        # instapy_job can be omitted
        instapy_job = 'Unfollowing users'
        telegram_bot.sendStartJob(instapy_job)

        session.unfollow_users(amount=random.randint(10,15), onlyInstapyFollowed = True, onlyInstapyMethod = 'FIFO', sleep_delay=random.randint(50,60))

        telegram_bot.sendEndJob(instapy_job)

        # Like
        hashtags = ['hashtag1','hashtag2']

        instapy_job = 'Liking by hashtags'
        telegram_bot.sendStartJob(instapy_job)

        session.like_by_tags(hashtags, amount=random.randint(9, 15))

        telegram_bot.sendEndJob(instapy_job)
    except:
        # If any error occurs, print it in console
        # and send a message containing the complete traceback
        import traceback
        error_traceback = traceback.format_exc()
        print(error_traceback)
        telegram_bot.sendError(error_traceback)
    finally:
        # end the script session
        session.end()


if __name__ == '__main__':
    run()
