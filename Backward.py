"""Backward"""
def main():
    """อ๋อไม่เข้าใจ"""
    box = []
    while True:
        message = input()
        if message == "NULL":
            break
        box.append(message)
    box.reverse()
    for i in box:
        print(i)
main()
