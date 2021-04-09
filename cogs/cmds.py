from discord.ext import commands
from asyncio import sleep
from exttt.myembeds import *


class Cmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["stressme", "stressmeout"])
    # check for blocked
    async def stress(self, ctx):
        async with ctx.typing():
            await sleep(0)
        await ctx.send(embed=e_stress(ctx.guild.id))

    @commands.command()
    async def help(self, ctx):
        async with ctx.typing():
            await sleep(0)
        await ctx.send(embed=e_help(ctx))


def setup(client):
    client.add_cog(Cmds(client))
