"""Muddled Menu"""
def main():
    """ Muddled Menu """
    food = input()
    box_list = []
    while food != "DONE":
        if food == "CLOSED" or food == "SOMETHING'S WRONG":
            box_list.clear()
            if food != "SOMETHING'S WRONG":
                break
        elif food[:8] == "Can't do":
            box_list.remove(food[10:])
        else:
            food = food.split(" #")
            if food[1] == "N":
                box_list.append(food[0])
            else:
                box_list.insert(int(food[1])-1, food[0])
        food = input()
    print("Full Course:", box_list, end=" ")
    box_list.reverse()
    print("Reversed:", box_list)
main()
