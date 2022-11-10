"""[Recommend] BTSMRT"""
def main():
    """[Recommend] BTSMRT"""
    day, age, height = input(), float(input()), float(input())
    if age < 14:
        if height < 90:
            print("FREE")
        elif height <= 140 and day == "Children Day":
            print("FREE")
        else:
            print("PAY")
    elif age >= 60 and day == "Senior Day":
        print("FREE")
    else:
        print("PAY")
main()
