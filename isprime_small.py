""" isprime_small """
def main():
    """ isprime_small """
    numfonnarak = int(input())
    if numfonnarak > 1:
        for i in range(2, numfonnarak):
            if (numfonnarak % i) == 0:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")
main()
