""" 3nPlus1 """
def main():
    """ 3nPlus1 """
    box_list = list()
    sus_box_list = list()
    nom = int(input())
    # total = 1
    while nom != 0:
        # number = nom
        box_list.append(nom)
        # while number > 1:
        #     if number % 2 == 0:
        #         number /= 2
        #     else:
        #         number = number*3 + 1
        #     total += 1
        # print(total)
        # total = 1
        nom = int(input())
    for i in box_list:
        while i != 1:
            if i % 2 == 0:#เลขคู่
                sus_box_list.append(i)
                i = i/2
            else:#เลขคี่
                i = (i*3)+1
                sus_box_list.append(i)
        print(len(sus_box_list) + 1)
        sus_box_list.clear()
main()
