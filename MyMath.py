""" MyMath """
import math
def main():
    """ ฝนไม่ชอบคณิต """
    question_1 = (math.sin(math.radians(90)) + math.sin(math.radians(60))**2) / \
        (math.cos(math.radians(245**2)) + math.cos(math.radians(45+135)))
    print(question_1)
    question_2 = (math.factorial(16) * math.factorial(4))/ math.factorial(8)
    print(question_2)
    question_3 = (15+25)/((((25-12)**2)+((12-15)**2))**0.5)
    print(question_3)
    question_4 = math.log10(1234**4)
    print(question_4)
    question_5 = (math.log(4234, 5) + math.log(8191, 2) + 71*math.log(156154, 10)) / \
        (math.log(777, 7) - math.log(888, 8) - math.log(999, 9))
    print(question_5)
main()
