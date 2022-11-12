""" Daydreamin """
def main():
    """ It's the way you walk
The way you talk
The way you make me feel inside
It's in your smile
It's in your eyes
I don't wanna wait for tonight """
    myfon = input()
    cutmyfon = int(myfon)
    kuy = ''
    if cutmyfon != 0:
        while cutmyfon > 0:
            kuy = str(cutmyfon % 2) + kuy
            cutmyfon //= 2
        print(kuy)
    else:
        print("0")
main()
