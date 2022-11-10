"""BrickBridge"""
def bridge():
    """BrickBridge"""
    brick_s = int(input())
    brick_m = int(input())
    goal = int(input())
    if goal > brick_m*5 + brick_s < goal:
        print("-1")
    elif goal <= brick_m*5 + brick_s:
        if goal == brick_m*5 + brick_s == goal:
            print(brick_s)
        elif goal//5 <= brick_m and brick_s >= (goal-(goal//5)*5):
            print(goal-(goal//5)*5)
        elif goal//5 > brick_m and brick_s >= (goal-(goal//5)*5):
            print(goal-brick_m*5)
        else:
            print("-1")
bridge()
