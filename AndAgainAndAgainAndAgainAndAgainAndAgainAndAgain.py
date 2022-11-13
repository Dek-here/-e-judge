""" AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain """
def main():
    """ AndKuyAndKuyAndKuyAndKuyAndKuyAndKuyAndKuy """
    text = input()
    aeiou = "aeiou"
    total, count = 0, 0
    text_list = text.replace(".", "").split(" ")
    for i in sorted(text_list):
        for k in aeiou:
            total += i.count(k)
        if total >= 2:
            print(i)
            count += 1
        total = 0
    if count == 0:
        print("Nope")
main()
