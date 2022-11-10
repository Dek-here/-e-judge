"""Cat Parade"""
def main():
    """Cat Parade"""
    arrange = []
    while True:
        temp = input()
        if temp == "END":
            break
        elif temp == "IT'S A DOG":
            arrange.reverse()
            arrange.pop(0)
            arrange.reverse()
        else:
            arrange.extend(temp.split(", "))
    comp_arrange = arrange.copy()
    arrange.sort()
    for i in arrange:
        position = comp_arrange.index(i) + 1
        numb = comp_arrange.count(i)
        for _ in range(numb-1):
            arrange.remove(i)
        print("%s %d %d" %(i, position, numb))
main()
