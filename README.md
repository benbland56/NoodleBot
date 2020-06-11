# NoodleBot
A Discord bot with some extra noodle

This bot uses python3

To use this bot you need the following packages

* discord.py

* dotenv.py

* asyncio.py

All can be installed with pip3 install "package" without quotations

To run the bot, first go through the usual process of adding a new application to your discord account.

Set this application to be a bot user, get your token and client ID, and add the bot to your channel. This is well documented here: https://realpython.com/how-to-make-a-discord-bot-python/#what-is-discord

Next clone the bot, and create a file called ".env" containing the token given to the discord bot you created.

This shoud look like: DISCORD_TOKEN="Token" without quotations

Then, add the ffmpeg file included with NoodleBot to your PATH environment variables as seen in this link here: https://windowsloop.com/install-ffmpeg-windows-10/

Then just run the bot with python3 bot.py and it should work just fine
