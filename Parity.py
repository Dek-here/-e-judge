"""Parity"""
def main(num, text):
    """8 bit even ood"""
    cout = 0
    for i in num:
        if i == "1":
            cout += 1
    cond_1 = (text == "Odd" and cout%2 != 0) or (text == "Even" and cout%2 == 0)
    cond_2 = (text == "Even" and cout%2 != 0) or (text == "Odd" and cout%2 == 0)
    if cond_1:
        num += "0"
    elif cond_2:
        num += "1"
    print(num)
main(input(), input())
