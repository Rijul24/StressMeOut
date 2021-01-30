import discord
import datetime
import os

rick = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

client = discord.Client()
update_here = [                                                                         # YYYY MM DD HH MM
               ["Polymers Quiz",            "2021 01 29 14 30", rick],
               ["Codechef Assignment",      "2021 01 30 22 00", "https://www.codechef.com/xxxxxxxxxxx"],
               ["Spectroscopy Assignment",  "2021 02 01 23 59", "https://drive.google.com/file/d/xxxxxxxxxxxxxx/view?usp=sharing"],
               ["Chemisrty practical",      "2021 02 02 23 59", "https://drive.google.com/file/d/xxxxxxxxxxxxxx/view?usp=sharing"]
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
    embeded=discord.Embed(color=0xFF5733)
    for i in range(len(update_here)):
        embeded.add_field(
            value = "[{}]({})".format(temp2[i], update_here[i][2]),
            name = "**" + update_here[i][0] + "**",
            inline = False
            )
    return embeded


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='you $stress out'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$stressme"):
        await message.channel.send(embed=to_print())
       
client.run(os.getenv('TOKEN'))                                                           # unique token for every discord bot
