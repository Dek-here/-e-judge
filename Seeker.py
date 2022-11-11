""" https://github.com/Dek-here """
def main():
    """ อายุ 19 มี github เป็นของตัวเองแล้วน้า """
    secret = input() + "K"
    fon = ""
    total = 0
    for i in secret:
        if i.isnumeric():
            fon += i
        else:
            if fon != "":
                total += int(fon)
                fon = ""
    print(total)
main()
