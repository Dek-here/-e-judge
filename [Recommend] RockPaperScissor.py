""" [Recommend] RockPaperScissor """
def main():
    """ AB """
    text = str(input())
    a_score = 0
    b_score = 0
    for i in range(0, len(text), 2):
        txt2word = text[i] + text[i+1]
        if text[i] == text[i+1]:
            pass
        elif txt2word == "SP" or txt2word == "RS" or txt2word == "PR":
            a_score += 1
        else:
            b_score += 1
    if a_score == b_score:
        print("DRAW", a_score)
    elif a_score > b_score:
        print("A win", str(a_score) + "-" + str(b_score))
    else:
        print("B win", str(b_score) + "-" + str(a_score))
main()
