import datetime
import discord
import gspread

rick = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
stick = "https://www.youtube.com/watch?v=Fclyy4JcibU"
snail = "https://www.youtube.com/watch?v=yOF86Uhnp0Q"
bun = "https://www.youtube.com/watch?v=T2-i3MoSJgs"


def get_list():                                                                   # imports the data from google sheet
    gc = gspread.service_account(filename="creds__.json")                         # private key
    sheet = gc.open("StressMeOut").sheet1
    data = sheet.get_all_records()
    length_list = len(data)
    final_list = [[0 for _ in range(3)] for _ in range(length_list)]              # final list that will contain name and deadlines

    for i in range(length_list):
        final_list[i][0] = data[i].get("TITLE")
        final_list[i][1] = data[i].get("YYYY MM DD HH mm")
        if data[i].get("LINK"):
            final_list[i][2] = data[i].get("LINK")
        else:
            final_list[i][2] = "https://www.youtube.com/watch?v=dQw4w9WgXcQ7"
        if not (final_list[i][0] and final_list[i][1]):
            final_list.pop(i)                                                     # removes the list with 'any' value missing

    return final_list


def to_left():
    update_here = get_list()
    current = datetime.datetime.now() + datetime.timedelta(hours=5, minutes=30)   # convert to ist
    temp = []
    for i in range(len(update_here)):
        temp.append(update_here[i][1])
        due = datetime.datetime.strptime(temp[i], '%Y %m %d %H %M')
        left = due - current                                                      # calculate the time remaining
        left = str(left)
        if left[0] == "-":
            temp[i] = "over"
        else:
            temp[i] = str(left)[0: len(left) - 10] + " Hours left"
    temp2 = temp
    embeded=discord.Embed(color=0x7289DA)
    for i in range(len(update_here)):
        embeded.add_field(                                                        # add different assignments as fields
            value = "[{}]({})".format(temp2[i], update_here[i][2]),
            name = "**" + update_here[i][0] + "**",
            inline = False
            )
    return embeded                                                                # returns the final embed
