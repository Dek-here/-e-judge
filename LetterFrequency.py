""" 死ぬのがいいわ """
def main():
    """ I want you to be my last
If I had to keep being separated from you like this
I would rather die """
    longsen = input().lower()
    fon = "0123456789'/<>,.?()-+*&^%$#@:!;=\\ฺ{}_~[] "
    for eyo in fon:
        longsen = longsen.replace(eyo, "")
    cutlongsen = (" ".join(longsen)).split(" ")
    nobi, letter = 0, ""
    for i in set(cutlongsen):
        amount = longsen.count(i)
        if amount > nobi:
            nobi = amount
            letter = i
    print(letter)
main()
