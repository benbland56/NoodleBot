#bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix ='!')

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

@bot.command(name = "Whos_a_cutey")
async def cutey(ctx):
    response = "Libs a cutey"
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


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command') 
bot.run(TOKEN)
