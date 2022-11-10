""" PointInCircle """

def main():
    """ print True/False """
    point_x = float(input(""))
    point_y = float(input(""))
    radius = float(input(""))
    define_point_x = float(input(""))
    define_point_y = float(input(""))
    distance = (((point_x-define_point_x)**2) + ((point_y-define_point_y)**2))**(1/2)
    if distance <= radius:
        print("True")
    else:
        print("False")
main()
