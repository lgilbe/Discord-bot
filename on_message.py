import discord
import random
from utils import *

# This file contains multiple on_message functions to be used in main.

async def roll(args, message):

    # Create embed
    rollEmbed = discord.Embed(color=0xFF0000)

    # Check if params are integers.
    for arguements in args:
        if hasInt(arguements) == False:
            rollEmbed.title = (":exclamation: Your input is invalid for !roll.")
            rollEmbed.description = "Please enter arguements of the type int."
            rollEmbed.set_author(name=message.author.nick, icon_url=message.author.avatar_url)
            await message.channel.send(embed=rollEmbed)
            return

    # Get num of params so we can send correct message
    if len(args) == 2:
        # Send roll
        num = random.randint(int(args[0]), int(args[1]))
        rollEmbed.title = (":game_die: " + message.author.nick + " rolled a " + str(num) + ".")
        rollEmbed.set_author(name=message.author.nick, icon_url=message.author.avatar_url)
        await message.channel.send(embed=rollEmbed)

    elif len(args) == 1:
        # Send roll
        num = random.randint(0, int(args[0]))
        rollEmbed.title = (":game_die: " + message.author.nick + " rolled a " + str(num) + ".")
        rollEmbed.set_author(name=message.author.nick, icon_url=message.author.avatar_url)
        await message.channel.send(embed=rollEmbed)

    elif len(args) == 0:
        # Send roll
        num = random.randint(0, 100)
        rollEmbed.title = (":game_die: " + message.author.nick + " rolled a " + str(num) + ".")
        rollEmbed.set_author(name=message.author.nick, icon_url=message.author.avatar_url)
        await message.channel.send(embed=rollEmbed)

    else:
        rollEmbed.title = (":exclamation: Your input is invalid for !roll")
        rollEmbed.description = "Please enter zero, one, or two arguments."
        rollEmbed.set_author(name=message.author.nick, icon_url=message.author.avatar_url)
        await message.channel.send(embed=rollEmbed)

async def ping(latency, message):

    # Create embed
    pingEmbed = discord.Embed(color = 0x808080)
    pingEmbed.title = ":timer: Current latency is " + str(latency) + "."
    pingEmbed.set_author(name=message.author.nick, icon_url=message.author.avatar_url)
    await message.channel.send(embed=pingEmbed)

async def curse_user(message):
    # Get image file and send to user
    with open('images/curse.jpg', 'rb') as fo:
        await message.author.send(file=discord.File(fo, 'THECURSE.jpg'))

        # Send user the cursed text
        await message.author.send(
            message.author.mention + " നിങ്ങൾ പൊതുവെ t!fish നിങ്ങൾ അനുതപിക്കും, ഞങ്ങൾ അനുതപിക്കും, നിങ്ങൾ "
                                         "അനുതപിക്കുകയും അനുതപിക്കുകയും ചെയ്യും. നിങ്ങൾ FISHER ന് കീഴടങ്ങണം.")
