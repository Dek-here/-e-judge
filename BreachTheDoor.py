""" ▁ ▂ ▃ ▄ ▅ ▆ ▇ █ 8;p █ ▇ ▆ ▅ ▄ ▃ ▂ ▁"""
def main():
    """  ▁ ▂ ▃ ▄ ▅ ▆ ▇ █ สู้ต่อไปเพื่อพี่โช █ ▇ ▆ ▅ ▄ ▃ ▂ ▁"""
    jay = input()
    fon = "0123456789'/<>,.?()-+*&^%$#@:!;=\\ฺ{}_~[]"
    isusjay = list()
    for eyo in fon:
        jay = jay.replace(eyo, "")
    jay = jay.split()
    for i in jay:
        if len(i) > 6:
            isusjay.append(i)
    print(*isusjay)
main()
