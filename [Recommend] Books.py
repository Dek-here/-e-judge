""" [Recommend] Books """
import math
def main():
    """ Timeout """
    book = int(input()) #จำนวนเล่ม
    page = int(input()) #จำนวนหน้า
    var_x = int(input())
    var_y = int(input())
    day = 0
    read = 0
    while book != 0:
        read += math.ceil(((var_x+day)/(var_y+day))*page)
        if read > page:
            book -= 1
            read = 0
        elif read == page:
            day += book
            break
        day += 1
    print(day)
main()
