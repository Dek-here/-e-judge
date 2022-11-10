"""Hamburger"""
def main():
    """hamburger"""
    bun1 = int(input())
    bun2 = int(input())
    print("|"*bun1 + "*"*(bun1+bun2)*2 + "|"*bun2)
main()
