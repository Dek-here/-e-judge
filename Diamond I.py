""" Diamond I """
def main():
    """ Diamond I """
    area = []
    deep = int(input())
    width = int(input())
    for _ in range(deep):
        area.extend((input().split()))
    most = 0
    for i in range(width):
        total = 0
        for k in range(0, deep*width, width):
            total += int(area[i+k])
        if total > most:
            most = total
    print(most)
main()
