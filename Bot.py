# Import discord lib
import discord

# Getting bot token from local.
with open("bot-info.txt") as FO:
    discordToken = FO.readline()

# Create a client for connection.
client = discord.Client()

# Client ready event - display stats
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord.')
    print(f'Current latency is: {client.latency}')
    for guild in client.guilds:
        print('Connected to: ' + guild.name)

# On message event
@client.event
async def on_message(message):
    print("In " + f'{message.channel}' + ", " +
     f'{message.author}' + " said: " + f'{message.content}')

# Run our client with token grabbed from local
client.run(discordToken)


