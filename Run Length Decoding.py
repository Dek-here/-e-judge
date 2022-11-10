""" Run Length Decoding """
def main():
    """ eiei """
    codeing = str(input())
    number = ""
    for i in codeing:
        if i.isalpha() == False:
            number += i
        else:
            print(i * int(number), end="")
            number = ""
main()
