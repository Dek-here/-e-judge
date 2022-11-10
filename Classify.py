""" Classify """
def main():
    """ Classify """
    number = input()
    box_list = list()
    cutdata = list()
    while number != "END":
        box_list.append(number)
        number = input()
    uncutdata = sorted(box_list)
    for i in uncutdata:
        cutdata.append(i[:4])
    last_year = 0
    for k in sorted(set(cutdata)):
        year = k[:2]
        if k[:2] == last_year:
            year = "--"
        print(year, int(k[2:4]), cutdata.count(k))
        last_year = k[:2]
main()
