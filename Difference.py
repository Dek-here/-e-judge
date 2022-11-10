""" Difference """
def main():
    """ Difference """
    box_seta = {()}
    box_setb = {()}
    nao = int(input())
    mao = int(input())
    for _ in range(nao):
        numa = int(input())
        box_seta.add(numa)
    for _ in range(mao):
        numb = int(input())
        box_setb.add(numb)
    box_setc = box_seta - box_setb #box_setc = box_seta.difference(box_setb)
    box_setc = sorted(box_setc)
    for i in box_setc:
        print(i, end=" ")
main()
