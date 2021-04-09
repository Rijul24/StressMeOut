import discord
from discord.ext import commands
import json


class Prefixes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open("_data.json", "r") as f:
            data = json.load(f)
        data[str(guild.id)] = {
            "1":
                {
                    "name": "sample assignment 1",
                    "dead": "2022 04 01 23 59"
                }
        }
        with open("_data.json", "w") as f:
            json.dump(data, f)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open("_data.json", "r") as f:
            data = json.load(f)
        data.pop(str(guild.id))
        with open("_data.json", "w") as f:
            json.dump(data, f)


def setup(client):
    client.add_cog(Prefixes(client))
