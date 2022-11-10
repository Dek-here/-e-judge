""" Frame """

def main():
    """ ไปต่อหรือพอแค่นี้? เพื่อนบอกควรถอย """
    word = input()
    for _ in range(len(word)+2):
        print("*", end="")
    print()

    print("*" + word + "*")

    for _ in range(len(word)+2):
        print("*", end="")
    print()

main()
