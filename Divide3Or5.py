""" Divide3Or5 """
def main():
    """ ควยไอสัสไม่อยากทำ """
    num = int(input())
    fon = 0
    for i in range(1, num+1):
        if i % 3 == 0 or i % 5 == 0:
            fon += i
    print(fon)
main()