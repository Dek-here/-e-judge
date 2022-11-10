""" [Recommend] SumOfNumber """
def main():
    """ print ค่าทั้งหมดที่เข้ามา """
    #ผลรวมครบ 100 = หยุด
    #input เข้ามาเป็น -1 = หยุด
    allnumber = 0
    number = 0
    iwantit = int(input())
    while allnumber != iwantit:
        number = int(input())
        if number == -1:
            break
        allnumber += number
    print(allnumber)
main()
