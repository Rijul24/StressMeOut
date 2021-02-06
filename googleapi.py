import gspread
# from pprint import pprint

gc = gspread.service_account(filename="creds__.json")
sheet = gc.open("StressMeOut").sheet1


def get_list():
    data = sheet.get_all_records()
    length_list = len(data)
    final_list = [[0 for _ in range(3)] for _ in range(length_list)]

    for i in range(length_list):
        final_list[i][0] = data[i].get("TITLE")
        final_list[i][1] = data[i].get("YYYY MM DD HH mm")
        if data[i].get("LINK"):
            final_list[i][2] = data[i].get("LINK")
        else:
            final_list[i][2] = "https://www.youtube.com/watch?v=dQw4w9WgXcQ7"
        if not (final_list[i][0] and final_list[i][1]):
            final_list.pop(i)
    
    return final_list[::-1]
