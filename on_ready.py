import discord

# This file contains multiple on_ready functions to be used in main.

async def printClientInfo(client):

    # Notify that the client is connected
    print(f'{client.user}' + ' has connected to Discord.')
    print("Current latency is: " + f'{client.latency}')

    # Print our connected Guilds
    for guild in client.guilds:
        print('Connected to: ' + guild.name)

async def updateClientStatus(client):
    # Change our status.
    await client.change_presence(status=discord.Status.online, activity=discord.Game(
        "Current members: " + str(client.get_guild(209539893708193793).member_count)))
