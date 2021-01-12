import discord
import datetime
import os

client = discord.Client()
update_here = [["Chemistry Practical",      "2021 01 12 23 59"],          # enter in 'MM DD HH MM'
               ["Unacademy Assignment 3",   "2021 01 13 22 00"],
               ["Chemistry MOT Assignment", "2021 01 14 23 59"],
               ["ESC Assignment 3",         "2021 01 15 23 59"],
               ["Math Quiz",                "2021 01 19 23 59"],
               ["Chemistry Quiz",           "2021 01 21 23 59"],
               # ["asdlkfjasdkfjl",           "2021 01 21 12 12"]
               ]


def to_left():
    current = datetime.datetime.now()
    temp = []
    for i in range(len(update_here)):
        temp.append(update_here[i][1])

    for i in range(len(temp)):
        due = datetime.datetime.strptime(temp[i], '%Y %m %d %H %M')
        left = due - current
        left = str(left)
        length_ = len(left)
        if left[0] == "-":
            temp[i] = "over"
        else:
            temp[i] = str(left)[0: length_ - 10] + " Hours left"
    return temp


def to_print():
    temp2 = to_left()
    print_this = str()
    for i in range(len(update_here)):
        print_this += update_here[i][0] + "\n\t\t\t\t\t\t" + temp2[i] + "\n"
    return print_this


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$stressme'):
        await message.channel.send(to_print())

client.run(os.getenv('TOKEN'))
