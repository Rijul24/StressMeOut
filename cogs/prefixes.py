import discord
from discord.ext import commands
import json
from exttt.myembeds import whatpref
from asyncio import sleep


class Prefixes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefixes[str(guild.id)] = "$"
        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefixes.pop(str(guild.id))
        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f)

    @commands.command(aliases=["changeprefix"])
    @commands.has_permissions(administrator=True)
    async def changepref(self, ctx, pref):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = pref
        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f)
        await ctx.send(f"new prefix is {pref}")

    @commands.command()
    async def prefix(self, ctx):
        async with ctx.typing():
            await sleep(0)
        await ctx.send(embed=whatpref(ctx))


def setup(client):
    client.add_cog(Prefixes(client))
