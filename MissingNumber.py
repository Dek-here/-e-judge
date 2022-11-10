""" MissingNumber """
def main(nao, box):
    """ MissingNumber """
    box_list = []
    while box != 0:
        box_list.append(box)
        box = int(input())
    for i in range(1, nao+1):
        if i not in box_list:
            print(i)
main(int(input()), int(input()))
