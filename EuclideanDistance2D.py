""" EuclideanDistance2D """

def main():
    """ printเหี้ยไร """
    num_q1 = float(input())
    num_q2 = float(input())
    num_p1 = float(input())
    num_p2 = float(input())
    ans = (((num_q1-num_p1)**2)+((num_q2-num_p2)**2))**(1/2)
    print(ans)
main()
