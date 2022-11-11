"""All_Primes"""
def main():
    """All_Primes"""
    num = int(input())
    result = 0
    for i in range(2, num+1):
        x_val = 0
        for j in range(2, i):
            if i%j == 0:
                x_val = 1
                break
        if x_val != 1:
            result += 1
    print(result)
main()
