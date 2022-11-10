""" PickThem """
def main(box):
    """ PickThem """
    check = 0
    box_list = box[1:-1].split(', ')
    for i in box_list:
        if int(i)%2 == 0:
            check = 1
            print(i)
    if check == 0:
        print("Nope")
main(input())
