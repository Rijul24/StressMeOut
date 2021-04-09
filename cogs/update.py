from discord.ext import commands
import json
import datetime


class Update(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add(self, ctx, *, tada):
        tada = tada.split(",")
        if len(tada) - 2:
            await ctx.send("please provide 2 comma seperated arguments\n\
                      eg $add sample 1, 2021 05 10 23 59")
            return
        try:
            due = datetime.datetime.strptime(tada[1].strip(), '%Y %m %d %H %M')
        except ValueError:
            await ctx.send("format of date should be YYYY MM DD HH mm\n\
                      eg $add sample 1, 2021 05 10 23 59")
            return
        with open("_data.json", "r") as f:
            _data = json.load(f)
        _data[str(ctx.guild.id)].append([tada[0].strip(), tada[1].strip()])
        _data[str(ctx.guild.id)].sort(key=lambda val: datetime.datetime.strptime(val[1], '%Y %m %d %H %M'))
        with open("_data.json", "w") as f:
            json.dump(_data, f)
        await ctx.send("**succesful**")

    @commands.command(aliases=["extend"])
    @commands.has_permissions(administrator=True)
    async def update(self, ctx, *, tada):
        tada = tada.split(",")
        print(tada)
        if len(tada) - 3:
            await ctx.send("please provide 3 comma seperated arguments\n\
                          eg $update 1, deadline, 2021 05 10 23 59\
                          eg $update 1, name, Sample assignment 3")
            return
        if tada[1].strip() == "deadline":
            tada[1] = 2
        else:
            tada[1] = 1
        if tada[1] == 2:
            try:
                due = datetime.datetime.strptime(tada[2].strip(), '%Y %m %d %H %M')
            except ValueError:
                await ctx.send("format of date should be YYYY MM DD HH mm\n\
                              eg $add sample 1, 2021 05 10 23 59")
                return
        with open("_data.json", "r") as f:
            _data = json.load(f)
        _data[str(ctx.guild.id)][int(tada[0]) - 1][tada[1] - 1] = tada[2].strip()
        _data[str(ctx.guild.id)].sort(key=lambda val: datetime.datetime.strptime(val[1], '%Y %m %d %H %M'))
        with open("_data.json", "w") as f:
            json.dump(_data, f)
        await ctx.send("**succesful**")

    @commands.command()
    @commands.check_any(commands.has_role("StressedOut"), commands.has_permissions(administrator=True))
    async def delete(self, ctx, pos):
        try:
            pos = int(pos)
        except ValueError:
            await ctx.send("enter valid int")
            return
        with open("_data.json", "r") as f:
            _data = json.load(f)
        if not 0 < pos < len(_data[str(ctx.guild.id)]):
            await ctx.send(f"enter a int between 1 and {len(_data[str(ctx.guild.id)])}")
            return
        _data[str(ctx.guild.id)].pop(pos - 1)
        with open("_data.json", "w") as f:
            json.dump(_data, f)
        await ctx.send("**succesful**")


def setup(client):
    client.add_cog(Update(client))
