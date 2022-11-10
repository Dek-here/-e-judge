""" Heron of Alexandria """
import math
def main():
    """ **(1/2), **0.5 """
    soma = float(input())
    somb = float(input())
    somc = float(input())
    sok = (soma + somb + somc)/2
    fonall = math.sqrt(sok * (sok - soma)*(sok - somb)*(sok - somc))
    print("%.3f" %fonall)
main()
