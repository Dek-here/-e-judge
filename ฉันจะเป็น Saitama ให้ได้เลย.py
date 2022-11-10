""" ฉันจะเป็น Saitama ให้ได้เลย """
import math
def main():
    """ Saitama """
    pushup = int(input())
    situp1 = int(input())
    situp2 = int(input())
    run = int(input())
    day_pushup = int(input())
    day_situp1 = int(input())
    day_run = int(input())
    day_situp2 = int(input())
    num1 = math.ceil(pushup/day_pushup)
    num2 = math.ceil(situp1/day_situp1)
    num3 = math.ceil(situp2/day_situp2)
    num4 = math.ceil(run/day_run)

    box = (num1, num2, num3, num4)
    box = sorted(box, reverse=True)
    for i in box:
        print(i)
        break

main()
        