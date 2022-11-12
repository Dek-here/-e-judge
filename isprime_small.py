""" isprime_small """
def main():
    """ isprime_small """
    numfonnarak = int(input())
    if numfonnarak > 1:
        for i in range(2, int(numfonnarak**0.5)+1):
            if (numfonnarak % i) == 0:
                print("NO")
                break
        else:
            print("YES")
    else:
        print("NO")
main()
