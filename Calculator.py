"""Calculator"""
def main():
    """Calculator"""
    num = int(input())
    press = 0
    if num == 1:
        press += 1
        print(press)
    else:
        for i  in range(1, num+1):
            press += (len(str(i))+1)
        print(press)
main()
