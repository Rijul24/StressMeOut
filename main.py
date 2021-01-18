import discord
import datetime
import os

client = discord.Client()
update_here = [                                                             # YYYY MM DD HH MM
               ["ESC Assignment 3",         "2021 01 15 23 59"],
               ["Math Quiz",                "2021 01 19 23 59"],
               ["Chemistry Quiz",           "2021 01 21 23 59"],
               ]

def to_left():                                                                          # creates a list containing time left
    current = datetime.datetime.now() + datetime.timedelta(hours=5, minutes=30)         # converts to IST
    temp = []
    for i in range(len(update_here)):
        temp.append(update_here[i][1])
        due = datetime.datetime.strptime(temp[i], '%Y %m %d %H %M')                     # converts str to datetime
        left = due - current                                                            # calculates time left
        left = str(left)                                                                # convertes to str
        if left[0] == "-":                                                              # if time negatve
            temp[i] = "over"
        else:
            temp[i] = str(left)[0: len(left) - 10] + " Hours left"                      # cuts seconds and macroseconds
    return temp


def to_print():
    temp2 = to_left()
    print_this = str()                                                                  # final string to be printed
    if len(update_here) == 0:                                                           # if nothing due
        print_this += "no pending work \ngo cover your backlog"
    else:
        for i in range(len(update_here)):
            print_this += update_here[i][0] + "\n\t\t\t\t\t\t" + temp2[i] + "\n"
    return "```python" + print_this + "```"


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$stressme'):
        await message.channel.send(to_print())

client.run(os.getenv('TOKEN'))                                                           # unique token for every discord bot
