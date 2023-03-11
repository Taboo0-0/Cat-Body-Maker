def cat_head():
    s = ""  #s is the string that is returned
    s = s + "   |\---/| \n"
    s = s + "   | o_o | \n"
    s = s + "    \_^_/  \n"
    return s

def cat_body(n):
    s = ""  #s is the string that is returned
    s = s + "     _ _\n"
    s = s + "   /     \ \n"
    for n in range(n):
        s = s + "   |     |\n"
    s = s + "   ------- \n"
    return s

def cat_legs(n):
    s = ""  #s is the string that is returned
    for n in range(n):
        s = s + "    |   |\n"
    s = s + "    m   m"
    return s


def make_cat():
    s = ""
    s += cat_head()
    s += cat_body(3)
    s += cat_legs(2)
    return s


