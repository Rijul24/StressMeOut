import discord
import os
# from keep_alive import keep_alive
from ssssss import ssssss
from to_print import to_print

client = discord.Client()

stress_cmds = ("$stress", "$stressme", "$strems", "stremsme", "$killme", "fknkillme")
ss_cmds = ("pls ssssss", "Pls ssssss")

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='you $stress out'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(stress_cmds):
        await message.channel.send(embed=to_print())
    if message.content.startswith(ss_cmds):
        await message.channel.send(ssssss(message.content))

# keep_alive()
client.run(os.getenv('TOKEN'))
