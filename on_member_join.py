import discord
from discord.utils import get

# This file contains multiple on_member_join functions to be used in main.

async def updateUserCount(client):
    # Update user count
    game = discord.Game("Current members: " + str(client.get_guild(209539893708193793).member_count))
    await client.change_presence(status=discord.Status.online, activity=game)


async def addDefaultRoles(client, member):
    # Get ids and convert them to role objects
    defaultID = 647903075763224598
    memberId = 223638410135339010
    defaultRole = get(client.guilds[0].roles, id=defaultID)
    memberRole = get(client.guilds[0].roles, id=memberId)

    # Add roles to new user
    await member.add_roles(defaultRole, reason="Adding default role on join!")
    await member.add_roles(memberRole, reason="Adding member role on join!")