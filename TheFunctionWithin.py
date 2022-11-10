""" TheFunctionWithin """

def main():
    """ main """
    var_a = float(input())
    var_b = float(input())
    var_c = float(input())
    var_d = float(input())
    print(fff(fff(var_a)))
    print(ggg(fff(var_a - var_b)))
    print(hhh(fff(var_a + var_b), fff(var_a + var_c), \
    ggg(fff(var_d ** 2))))
    print(iii(hhh(fff(var_a + var_b), fff(var_a - var_c), \
    ggg(fff(var_d ** 2))), ggg(fff(var_a - var_b)), \
    (fff(fff(fff(fff(fff(var_c)))))), (var_d ** 8)))
def fff(num):
    """ f """
    return 2 * num
def ggg(num2):
    """ g """
    return (3 * (num2 ** 4)) - (num2 ** 3) + (2 * (num2 ** 2)) + 10
def hhh(num1, num2, num3):
    """ h """
    return (num3+num1)**2 - (num1*num2) + (num2**2)
def iii(num1, num2, num3, num4):
    """ i """
    return ((num1**2)+(num2**2)-(num3**2))/((num4**2)-(2*num1*num4)\
        + (2*num1))
main()
