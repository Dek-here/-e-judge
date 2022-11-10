""" All_Primes """

def main():
    """ All_Primes """
    numfonnarak = int(input())
    prime = 0
    for i in range(2, numfonnarak):
        for a in range(2, i):
            if i % a != 0:
                prime += 1
    print(prime)
main()