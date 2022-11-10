"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""

def main():
    """Ascend or Descend"""
    num_str = str(input())
    if num_str == "Ascend":
        num_1, num_2, num_3 = float(input()), float(input()), float(input())
        if num_1 > num_2:
            num_1, num_2 = num_2, num_1
        if num_2 > num_3:
            num_2, num_3 = num_3, num_2
        if num_1 > num_2:
            num_1, num_2 = num_2, num_1
        print("%.2f, %.2f, %.2f" %(num_1, num_2, num_3))
    elif num_str == "Descend":
        num_1, num_2, num_3 = float(input()), float(input()), float(input())
        if num_1 < num_2:
            num_1, num_2 = num_2, num_1
        if num_2 < num_3:
            num_2, num_3 = num_3, num_2
        if num_1 < num_2:
            num_1, num_2 = num_2, num_1
        print("%.2f, %.2f, %.2f" %(num_1, num_2, num_3))
main()
