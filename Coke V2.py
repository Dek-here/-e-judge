""" https://github.com/Dek-here """
def main(prize, clover, pro_prize, needed_coke):
    """ อายุ 19 มีอีโก้เป็นของตัวเอง """
    if clover == 0:
        return print(prize * needed_coke)
    can_dis = needed_coke // clover
    pro_prize = prize - pro_prize
    if needed_coke % clover == 0 and can_dis != 0:
        can_dis = can_dis - 1
    print((prize * needed_coke) - (can_dis * pro_prize))
main(int(input()), int(input()), int(input()), int(input()))
