def ssssss(s):
    s = s[11:]
    s = s.replace("are", "r")
    s = s.replace("you", "u")
    s = s.replace("wait", "w8")
    s = s.replace("what", "wt")
    s = list(s)
    final = ""
    for i in s:
        i = list(i)
        for j in i:
            if j in "aeio":
                pass
            else:
                final += j
    return final