# https://discordpy.readthedocs.io/en/latest/index.html
# Imports
import discord
from on_message import *
from discord.utils import get

# Getting bot token from local.
with open("bot-info.txt") as FO:
    discordToken = FO.readline()

# Create a client for connection.
client = discord.Client()

# Client ready event - display stats
@client.event
async def on_ready():
    print(f'{client.user}' + ' has connected to Discord.')
    print("Current latency is: " + f'{client.latency}')

    # Print our connected Guilds
    for guild in client.guilds:
        print('Connected to: ' + guild.name)

    # Change our status.
    await client.change_presence(status=discord.Status.online, activity=discord.Game(
        "Current members: " + str(client.get_guild(209539893708193793).member_count)))

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

        await message.channel.send("Command: " + command)
        await message.channel.send("Args: " + str(args))

        # Begin commands

        if command == "roll":
            await roll(args, message)
        if command == "ping":
            await ping(round(client.latency*1000), message)

    # Easter egg if user doesn't use correct channel to fish
    if message.content.startswith("t!fish"):
        if message.channel.id == 209539893708193793:
            await curse_user(message)

# On join handler
@client.event
async def on_member_join(member):

    # Update user count
    game = discord.Game("Current members: " + str(client.get_guild(209539893708193793).member_count))
    await client.change_presence(status=discord.Status.online, activity=game)

    # Get ids and convert them to role objects
    defaultID = 647903075763224598
    memberId = 223638410135339010
    defaultRole = get(client.guilds[0].roles, id=defaultID)
    memberRole = get(client.guilds[0].roles, id=memberId)

    # Add roles to new user
    await member.add_roles(defaultRole, reason="Adding default role on join!")
    await member.add_roles(memberRole, reason="Adding member role on join!")


# On leave handler
@client.event
async def on_member_remove(member):
    game = discord.Game("Current members: " + str(client.get_guild(209539893708193793).member_count))
    await client.change_presence(status=discord.Status.online, activity=game)

# Error handler - todo
@client.event
async def on_error(event):
    print(event)

# Run our client with token grabbed from local
client.run(discordToken)
