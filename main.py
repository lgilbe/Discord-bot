# https://discordpy.readthedocs.io/en/latest/index.html

# Imports
import discord
from on_message import *
from on_ready import *
from on_member_join import *
from on_error import *

# Getting bot token from local.
with open("bot-info.txt") as FO:
    discordToken = FO.readline()

# Create a client for connection.
client = discord.Client()

# Client ready event - display stats
@client.event
async def on_ready():

    # Print client info
    await printClientInfo(client)

    # Change our status.
    await updateClientStatus(client)

# On message handler
@client.event
async def on_message(message):

    # See if user message is a command with prefix //
    if message.content.startswith("+"):

        # Break down user message for interpreting.
        messageContent = message.content[1:].lower()
        args = messageContent.split()
        command = args[0]
        del(args[0])

        # Begin commands
        if command == "roll":
            await roll(args, message)
        elif command == "ping":
            await ping(round(client.latency*1000), message)

    # Easter egg if user doesn't use correct channel to fish
    if message.content.startswith("t!fish"):
        if message.channel.id == 209539893708193793:
            await curse_user(message)

# On join handler
@client.event
async def on_member_join(member):

    # Update user count
    updateUserCount(client)

    # Give new member all default roles
    addDefaultRoles(client, member)


# On leave handler
@client.event
async def on_member_remove(member):

    # Update user count
    updateUserCount(client)

# Error handler - print and log errors.
@client.event
async def on_error(event, *args, **kwargs):
    printError(event, *args, **kwargs)

# Run our client with token grabbed from local
client.run(discordToken)
