def grab_thirteenth_donut(donuts):
    return donuts[12]


def get_celebration_treat(treats):
    try:
        thirteenth_donut = grab_thirteenth_donut(treats)
    except IndexError as err:
        print("error info:", err)
        return "no donut :("

    return f"celebration {thirteenth_donut}!"

get_celebration_treat([])