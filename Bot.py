# Import discord api
import discord

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
    game = discord.Game("Current members: " + str(client.get_guild(209539893708193793).member_count))
    await client.change_presence(status=discord.Status.online, activity=game)

# On message event, log event.
@client.event
async def on_message(message):
    print("In " + f'{message.channel}' + ", " +
     f'{message.author}' + " said: " + f'{message.content}')

# On join event, update our user count.
@client.event
async def on_member_join(member):
    game = discord.Game("Current members: " + str(client.get_guild(209539893708193793).member_count))
    await client.change_presence(status=discord.Status.online, activity=game)

# On leave event, update our user count.
@client.event
async def on_member_remove(member):
    game = discord.Game("Current members: " + str(client.get_guild(209539893708193793).member_count))
    await client.change_presence(status=discord.Status.online, activity=game)

# Run our client with token grabbed from local
client.run(discordToken)


