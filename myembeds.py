import discord
from get_data import conv_list
# from exttt.main import get_pref


def e_stress(guild_id):
    res = conv_list(guild_id)
    embeded = discord.Embed(color=0x7289DA)
    for i in range(len(res)):
        embeded.add_field(
            value=format(res[i][1]),
            name="**" + str(res[i][0]) + "**",
            inline=False
            )
    return embeded


def e_help(guild_id):
    embeded = discord.Embed(
        color=0x00FF00,
        title="Command List",
        description="""my prefix in this server is {prefix}
                       source code can be found (here)[{limk}]
                       (invite link)[{invite_link}]"""
    )
    embeded.add_field(
            value="$$changepref {new prexif}/ $$changeprefix {new prefix}\n(without curly brackets)",
            name="**To change the prefix of bot**",
            inline=False
    )
    embeded.add_field(
        value="$$Stress\naliases -> ($$StressMe, $$StressMeOut)",
        name="**~~stress~~**",
        inline=False
    )
    return embeded


def e_miss_perm_admin():
    embeded = discord.Embed(
        color=0xFF0000,
        title="Missing Permissions",
        description="""You're missing permissions to run this command.\n\
        This command is marked as Admin only."""
        )
    return embeded


def e_miss_perm_owner():
    embeded = discord.Embed(
        color=0xFF0000,
        title="Missing Permissions",
        description="""You're missing permissions to run this command.\n\
        This command can only be used by Bot Owner."""
        )
    return embeded


def e_miss_perm_role():
    embeded = discord.Embed(
        color=0xFF0000,
        title="Missing Role",
        description="""You're missing permissions to run this command.\n\
        This command can only be used by members with "StressMe" role and Administrator."""
        )
    return embeded


def whatpref(ctx):
    embeded = discord.Embed(
        color=0x0000FF,
        title="StressMeOut Prefixes",
        description="""Bots custom prefix in this server is {get_pref("a", ctx)[0]}.\n\
            Bots Universal prefix is ' **';,** '
            You can also mention the bot
            You can change prefix using ('changepref' or 'changeprefix') command
            eg \" **';,change prefix %** \" to set % as prefix"""
    )
    return embeded
