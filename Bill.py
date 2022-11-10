"""Bill"""
def main():
    """ eiei """
    foodprize = int(input())
    servicerate = 0.1 #10%
    vat = 0.07 #7%
    servicecharge = foodprize * servicerate
    if servicecharge > 1000:
        servicecharge = 1000
    elif servicecharge < 50:
        servicecharge = 50
    vatprize = (foodprize + servicecharge) * vat
    total = (foodprize + servicecharge) + vatprize
    print('%.2f' %total)
main()
