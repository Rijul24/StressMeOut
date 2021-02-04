import datetime
import discord
from list_data import update_here

def to_left():
    current = datetime.datetime.now() + datetime.timedelta(hours=5, minutes=30)
    temp = []
    for i in range(len(update_here)):
        temp.append(update_here[i][1])
        due = datetime.datetime.strptime(temp[i], '%Y %m %d %H %M')
        left = due - current
        left = str(left)
        if left[0] == "-":
            temp[i] = "over"
        else:
            temp[i] = str(left)[0: len(left) - 10] + " Hours left"
    return temp


def to_print():
    temp2 = to_left()
    embeded=discord.Embed(color=0x7289DA)
    for i in range(len(update_here)):
        embeded.add_field(
            value = "[{}]({})".format(temp2[i], update_here[i][2]),
            name = "**" + update_here[i][0] + "**",
            inline = False
            )
    return embeded
