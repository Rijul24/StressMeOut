import discord
import os
from keep_alive import keep_alive
from ssssss import ssssss
from to_print import to_left
from update import update

client = discord.Client()

stress_cmds = ("$stress", "$strems", "$killme", "fuvvingkillme")
ss_cmds = ("pls ssssss")

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))                                                 # prints on teminal when logged in
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='you $stress out'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower().startswith(stress_cmds):
        await message.channel.send(embed=to_left())                                                        # sends the text with assignment name and time remaining
    if message.content.lower().startswith(ss_cmds):                                                        # removes all vowels from the text
        await message.channel.send(ssssss(message.content.lower()))                                        
    if message.content.lower().startswith('$update') and message.author.id == 00000000000:                 # my unique user id
        l = list(message.content.split("|"))                                                               
        l[0] = l[0][7:].strip()
        await message.channel.send(update(l))                                                              # update the google sheets

keep_alive()                                                                                               # pings the bot every 5 mins
client.run(os.getenv("TOKEN"))                                                                             # unique discord token
