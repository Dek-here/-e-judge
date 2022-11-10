""" PickThemAgain """
def main(box):
    """ PickThemAgain """
    check = 0
    box_list = box.split()
    box_list.reverse()
    for i in box_list:
        if int(i)%3 == 0 or int(i)%5 == 0:
            check = 1
            print(i)
    if check == 0:
        print("Nope")
main(input())
