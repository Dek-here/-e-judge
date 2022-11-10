""" เรนนี่เองคั๊บมุมุ ❤｡◕‿◕｡"""
import json
def main():
    """ ไอสัสเจย์หน้าหมา """
    box_dict = dict()
    jay = input()
    score = float(input())
    box_dict.update(json.loads(jay))
    fon = list(filter(lambda var: var[1] >= score, box_dict.items()))
    fon.sort()
    if fon == list():
        print("Nope")
    else:
        for key, value in fon:
            print(key+"\t"+"%.2f"%(value))
main()
