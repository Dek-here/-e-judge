""" ควย """

def main():
    """ ควยโค๊ดเหี้ยหน้าหีหมา """
    numa = int(input())
    numb = int(input())
    numc = int(input())
    numd = int(input())
    okay_letgo = (numd//(numb+numc))*(numb+numc)
    if okay_letgo < numd:
        if numd-okay_letgo >= numb:
            okay_letgo += ((numd-okay_letgo)//numb)*(numb+numc)
        else:
            okay_letgo += numd-okay_letgo
    cost = (okay_letgo-((okay_letgo//(numb+numc))*numc))*numa
    print(cost, okay_letgo)
main()
