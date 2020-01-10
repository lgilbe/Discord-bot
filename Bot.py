# https://discordpy.readthedocs.io/en/latest/index.html
# Imports
import discord
from discord.ext import commands
from discord.utils import get
import random
import time

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
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Current members: " + str(client.get_guild(209539893708193793).member_count)))

# On message events
@client.event
async def on_message(message):

    # Will roll between 0,100 and print your roll.
    if message.content.lower() == "!roll":
        if f'{message.author}'== "AkChaseKid#0354":
            num = random.randint(0,1)
            if num == 0:
                num = random.randint(0,11)
                await message.channel.send("> :game_die:  " + f'{message.author}' + " rolled " + str(num))
            else:
                num = random.randint(0,101)
                await message.channel.send("> :game_die:  " + f'{message.author}' + " rolled " + str(num))
        else:
            print(message.author)
            num = random.randint(0,101)
            await message.channel.send("> :game_die:  " + f'{message.author}' + " rolled " + str(num))

    # Allows you to test bot ping.
    if message.content.lower() == "!ping":
        ping = str(round(client.latency*1000))
        await message.channel.send("> Current latency is " + ping)
        
    #Adds our default roles to users if they don't have it.
    if message.content.lower() == "!defaultroles":
        defaultID = 647903075763224598
        defaultRole = get(client.guilds[0].roles, id=defaultID)
        count = 0

        for member in client.guilds[0].members:
            if defaultRole not in member.roles:
                await member.add_roles(defaultRole)
                count = count + 1
        if count == 0:
            await message.channel.send("> No users needed a role.")
        else:
            await message.channel.send("> Added default roles to " + str(count) + " members")

    #Log user messages.
    print("In " + f'{message.channel}' + ", " +
     f'{message.author}' + " said: " + f'{message.content}')

# On join event, update our user count and assign roles.
@client.event
async def on_member_join(member):
    game = discord.Game("Current members: " + str(client.get_guild(209539893708193793).member_count))
    await client.change_presence(status=discord.Status.online, activity=game)

    #Apply our default roles
    defaultID = 647903075763224598
    defaultRole = get(client.guilds[0].roles, id=defaultID)
    await member.add_roles(defaultRole)

# On leave event, update our user count.
@client.event
async def on_member_remove(member):
    game = discord.Game("Current members: " + str(client.get_guild(209539893708193793).member_count))
    await client.change_presence(status=discord.Status.online, activity=game)

# Run our client with token grabbed from local
client.run(discordToken)


