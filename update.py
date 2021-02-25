import gspread


def add(namee, deadd, where):                                      # add a row
  gc = gspread.service_account(filename="creds__.json")
  sheet = gc.open("StressMeOut").sheet1
  sheet.insert_row([namee, deadd], where)
  return '**successfully updated**'


def dell(row):                                                    # delete a row
  gc = gspread.service_account(filename="creds__.json")
  sheet = gc.open("StressMeOut").sheet1
  sheet.delete_row(row)
  return '**successfully deleted**'


def modify(x, y, new):                                           # change value
  gc = gspread.service_account(filename="creds__.json")
  sheet = gc.open("StressMeOut").sheet1
  sheet.update_cell(x, y, new)
  return '**successfully updated**'



def update(mylist):                                              # input -> list, l[0] -> what to do
  if mylist[0] == 'add' or mylist[0] == '+':
    return add(mylist[1].strip(), mylist[2].strip(), 1+int(mylist[3].strip()))
  if mylist[0] == 'del' or mylist[0] == '-':
    return dell(1+int(mylist[1].strip()))
  if mylist[0] == 'modify' or mylist[0] == '*':
    return modify(1+int(mylist[1].strip()), int(mylist[2].strip()), mylist[3].strip())
  
