""" AscendingSort """
def main():
    """ AscendingSort """
    box = []
    for _ in range(5):
        number = int(input())
        box.append(number)
    box.sort()
    for i in range(len(box)):
        print(box[i])
main()
