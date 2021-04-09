import os
import json
import discord
from discord.ext import commands
from time import time
from asyncio import sleep
import myembeds

print("Initializing...")
_bot_mention = "<@!798262042669613083> "


def is_me(ctx):
    return ctx.message.author.id == 762615112385036288


def get_pref(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    res = prefixes.get(str(message.guild.id))
    return res, _bot_mention, "';,"
# ~universal perfix~ = ';,


intents = discord.Intents.all()
client = commands.Bot(
    command_prefix=get_pref,
    intents=intents,
    case_insensitive=True,
    help_command=None,
    when_mentioned=True
)

"""
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=myembeds.e_miss_perm_admin())
        return
    if isinstance(error, commands.CheckFailure):
        await ctx.send(embed=myembeds.e_miss_perm_owner())
        return
    print(error)
"""


@client.command()
@commands.check(is_me)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send("**successful**")


@client.command()
@commands.check(is_me)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send("**successful**")


@client.command()
@commands.check(is_me)
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    await ctx.send("**successful**")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


# Run the bot with the token
client.run("Nzk4MjYyMDQyNjY5NjEzMDgz.X_yddQ.m6Zq175WV2auVyA8kiG0mBK9OCQ")
