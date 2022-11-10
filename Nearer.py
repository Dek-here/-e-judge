""" Nearer """
def main():
    """ มันเป็นไรอะ """
    alice = int(input())
    bob = int(input())
    icecream = int(input())
    a_ice = abs(icecream - alice)
    b_ice = abs(icecream - bob)
    if a_ice == b_ice:
        print("Sundaes", str(a_ice))
    elif a_ice < b_ice:
        print("Alice", str(abs((a_ice))))
    else:
        print("Bob", str(abs((b_ice))))
main()
