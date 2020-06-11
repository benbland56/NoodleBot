#bot.py
import os
import random
from discord import VoiceChannel
from discord import Spotify
import discord 
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = Bot(command_prefix ='!')

##Reads the file containing blacklisted words
with open("bad_words.txt") as file:
    bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]

# Event for NoodleBot connecting to server
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


##Commands
@bot.command(name = "test", help = "Test message because i'm bad at python so who knows when this bot is gonna work")
async def test(ctx):
    response = "Yup i do be kinda working tho"
    await ctx.send(response)

@bot.command(name = "roast_me")
async def roast(ctx):
    response = "I'd offer you some gun but your smile has plenty"
    await ctx.send(response)

@bot.command(name = "Hey_noodle")
async def cutey(ctx):
    response = "Sup kid"
    await ctx.send(response)


@bot.command(name ="oweh")
async def cheek(ctx):
    response = "I ain't working bruv"
    await ctx.send(response)

@bot.command(name = "roll_dice", help = "Send the command, followed by 2 numbers. The first being the number of dice, the second being the number of sides each dice has")
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [str(random.choice(range(1, number_of_sides + 1))) for _ in range(number_of_dice)]
    await ctx.send(', '.join(dice))

#Revisit
@bot.command(name = "create-channel")
@commands.has_role('Bot tester')
async def create_channel(ctx, channel_name):
    guild = ctx.guild
    print (channel_name)
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)   
        response = "Channel made"
        await ctx.send(response)
    else:
        return

##Small game for guessing numbers, will give level rewards for winning
@bot.command(name = "guess-the-number")
async def guess (ctx, number_guess: int):
    number = random.randint(1, 5)
    if number_guess == number:
        response = "Congrats you guessed it! Don't get anything though"
        await ctx.send(response)
    elif number_guess != number:
        response = "Better luck next time buddy, the number was "
        answer = number
        await ctx.send(response)
        await ctx.send(answer)

##Allows NoodleBot to join a voice channel when a given message is sent
@bot.command(name = "Join")
@commands.has_role('Bot tester')
async def on_message(message):
        author = message.author
        voice = author.voice.channel
        await VoiceChannel.connect(voice)

##Test Spotify intergration
@bot.command(name = "TrackName")
async def spotify (ctx, user: discord.Member=None):
    user = user or ctx.author
    print (user)
    for activity in user.activities:
        if isinstance(activity, Spotify):
                await ctx.send(f"{user} is listening to {activity.title} by {activity.artist}")
        else:
            print("oops")
            return

##Removes any messages contained in the bad_words.txt file
@bot.event
async def on_message(message):
    message_content = message.content.strip().lower()
    for bad_word in bad_words:
        if bad_word in message_content:
            await message.delete()
            response = "Naughty Naughty"
            channel = message.channel
            await channel.send(response)
    await bot.process_commands(message)

##Returns an error if a user doesn't have correct permissions to use the bot
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command')

bot.run(TOKEN)
