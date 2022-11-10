""" Sequence VI """

def main():
    """ ตัวตึงมากๆ """
    num = int(input())
    for row in range(num):
        for eiei in range(row+1):
            print(eiei+1, end=" ")
        print() 
main()
