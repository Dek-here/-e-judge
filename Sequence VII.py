""" Sequence VII """

def main():
    """ แล้วกูมี for 4 ตัวค้าบน้องๆอิอิ"""
    num = int(input())
    for row in range(num): #แถวบรรทัด num = บรรทัด
        for eiei in range(row+1): #เขียนเนื้อหา
            print(eiei+1, end=" ")
        print()
    for row in range(num-1):
        for eiei in range(num-(row+1)):
            print(eiei+1, end=" ")
        print()
main()
