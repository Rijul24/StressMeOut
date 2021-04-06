from discord.ext import commands
import discord
import json
from stress import stress_e
from time import time
from asyncio import sleep

print("Initializing...")
_bot_mention = "<@!798262042669613083>"
welp = "https://github.com/armaanbadhan/StressMeOut/blob/main/help.md"


def is_me():
    def predicate(ctx):
        return ctx.message.author.id == 762615112385036288
    return commands.check(predicate)


def is_guild_owner():
    def predicate(ctx):
        return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id
    return commands.check(predicate)


def get_pref(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    res = prefixes.get(str(message.guild.id))
    if res is None:
        return "$"
    return res


intents = discord.Intents.all()
client = commands.Bot(command_prefix=get_pref, intents=intents, case_insensitive=True, help_command=None)


@client.event
async def on_ready():
    await client.change_presence(
        # status=discord.Status.dnd,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name='you $stress out'
        )
    )
    print(f"Logged in as {client.user}")
    print("-----------------------------")


# updates the json file on guild join (works)
# the guild id with 1 sample task in _data.json
@client.event
async def on_guild_join(guild):
    # for prefixes
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = "$"
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f)

    # for _data
    with open("_data.json", "r") as f:
        data = json.load(f)
    data[str(guild.id)] = {"1":
        {
            "name": "sample assignment 1",
            "dead": "2022 04 01 23 59"
        }
    }
    with open("_data.json", "w") as f:
        json.dump(data, f)


# when removed from a guild, delete data from both prefixes.json and _data.json
@client.event
async def on_guild_remove(guild):
    # for prefixes
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f)

    # for _data
    with open("_data.json", "r") as f:
        data = json.load(f)
    data.pop(str(guild.id))
    with open("_data.json", "w") as f:
        json.dump(data, f)


# changing the bot prefix
# need to check for correct premissions ##################
@client.command(aliases=["changeprefix"])
@commands.check_any(commands.is_owner(), is_guild_owner())
async def changepref(ctx, pref):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = pref
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f)
    await ctx.send(f"new prefix is {pref}")


# just for testing, comment before deploying!!!###########
@client.command(name="test")
async def foo(ctx, *, arg):
    start = time()
    async with ctx.typing():
        await sleep(0)
    await ctx.send(arg)
    await ctx.send(f"{(time() - start)} sec")


###################################################
###################################################
@client.command(aliases=["stressme", "stressmeout"])
async def stress(ctx):
    start = time()
    async with ctx.typing():
        await sleep(0)
    await ctx.send(embed=stress_e(ctx.guild.id))
    # stress_e(ctx.guild.id)
    await ctx.send(f"{(time() - start)} sec")     # remember to delete
##################################################
##################################################


# permissions?????
# role?
# lmfao
@client.command()
async def add(ctx, *, arg):
    pass


@client.command()
async def delete(ctx, *, arg):
    pass


@client.command()
async def update(ctx, *, arg):
    pass


@client.command()
async def huehuehue(ctx, *, arg):
    pass


@client.command()
async def ssup_bot(ctx, *, arg):
    await ctx.send("ssup owner")


'''
@client.command_prefix(get_pref)
async def when_mentioned(bot, ctx):
    ctx = ctx.strip()
    if ctx in None:
        await ctx.send("my prefix here is {lmao}")
'''

# Run the bot with the token
client.run("0000000000000000000000000")

# print(f"used in guild {ctx.guild}({ctx.guild.id}) by {ctx.author}({ctx.author.id}),"
#       f" channel={ctx.channel}({ctx.channel.id})")
