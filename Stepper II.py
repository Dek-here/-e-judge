""" Stepper II """

def main():
    """ คิดไม่ออก """
    mmm = int(input())
    nnn = int(input())
    if nnn >= mmm:
        for i in range(mmm, nnn+1):
            print(i)
    else:
        for i in range(mmm, nnn-1, -1):
            print(i)

main()
