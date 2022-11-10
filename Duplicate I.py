""" Duplicate I """
def main():
    """ Duplicate I """
    mao = int(input())
    nao = int(input())
    box_set1 = set()
    box_set2 = set()
    for _ in range(mao):
        id_stu1 = int(input())
        box_set1.add(id_stu1)
    for _ in range(nao):
        id_stu2 = int(input())
        box_set2.add(id_stu2)
    box_set3 = box_set1 & box_set2 #box_set3 = box_set1.intersection(box_set2)
    box_set3 = sorted(box_set3, reverse=True)
    if len(box_set3) == 0:
        print("Nope")
    else:
        for i in box_set3:
            print(i)
main()
