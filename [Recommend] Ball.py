"""[Recommend]"""
def main(height):
    """Ball"""
    count = 0
    if height >= 0.01:
        count = -1
        while height >= 0.01:
            count += 1
            height *= (3/5)
    print(count)
main(float(input()))
