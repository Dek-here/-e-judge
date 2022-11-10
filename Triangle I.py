""" Triangle I """

def main(var_a, var_b, var_c):
    """ Triangle I > +- 0.01 """
    if var_a**2 + var_b**2 == var_c**2 \
        or var_a**2 + var_c**2 == var_b**2 \
            or var_c**2 + var_b**2 == var_a**2:
        print("Yes")
    elif var_a**2 + var_b**2 > (var_c**2) - 0.01 and var_a**2 + var_b**2 < (var_c**2) + 0.01 \
        or var_a**2 + var_c**2 > (var_b**2) - 0.01 and var_a**2 + var_c**2 < (var_b**2) + 0.01 \
            or var_c**2 + var_b**2 > (var_a**2) - 0.01 and var_c**2 + var_b**2 < (var_a**2) + 0.01:
        print("Yes")
    else:
        print("No")

main(var_a=float(input()), var_b=float(input()), var_c=float(input()))
