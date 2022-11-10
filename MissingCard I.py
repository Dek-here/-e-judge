""" MissingCard I """
def main():
    """ yoghurt """
    column = ['S', 'H', 'D', 'C']
    row = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    box_list = list()
    box_set = set()
    por_set = set()
    for i in row:
        for aor in column:
            box_list.append(i+aor)
    box_set.update(box_list)
    for _ in range(51):
        por = input()
        por_set.add(por)
    jay_set = box_set - por_set
    print(*jay_set)
main()
