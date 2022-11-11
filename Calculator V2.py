"""hhh"""
def main(num):
    """jj"""
    before = str(len(num)-1) + '8' * (len(num)-1)
    back = (int(num)-int('9'*(len(num)-1) if len(num) != 1 else '0'))*(len(num)+1)
    print(int(before)+back if int(before)+back != 2 else 1)
main(input())
