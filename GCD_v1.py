"""GCD_v1"""
def main():
    """GCD_v1"""
    min_num = int(input())
    max_num = int(input())
    if min_num > max_num:
        min_num, max_num = max_num, min_num
    while min_num != 0:
        left = max_num%min_num
        max_num = min_num
        min_num = left
    print(max_num)
main()
