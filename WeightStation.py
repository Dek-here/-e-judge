""" ส่องหาพ่อมึงอะ """

def main():
    """ WeightStation เกลียดแม่งชิบหายโค๊ด """
    avr4wheel = float(input())
    wheel2 = float(input())
    wheel3 = float(input())
    wheel4 = float(input())

    wheel1 = 4*avr4wheel - wheel2 - wheel3 - wheel4
    if wheel1 + wheel2 + wheel3 + wheel4 > 15000:
        print("Overweight")
    elif abs(avr4wheel - wheel1) > avr4wheel/2 or abs(avr4wheel - wheel2) > avr4wheel/2 \
        or abs(avr4wheel - wheel3) > avr4wheel/2 or abs(avr4wheel - wheel4) > avr4wheel/2:
        print("Unbalance")
    else:
        print("Pass", '%.2f' % wheel1)
main()
