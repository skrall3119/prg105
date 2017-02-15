def main():
    loan = int(input("Enter your monthly loan payment: "))
    insurance = int(input("Enter your monthly insurance payment: "))
    gas = int(input("Enter the amount you spend on gas monthly: "))
    tires = int(input("Enter the amount you spend on tires monthly: "))
    maintenance = int(input("Enter the cost to maintain your vehicle: "))

    monthlyCosts = addCosts(loan, insurance, gas, tires, maintenance)
    yearlyCosts = calculateYearlyCost(monthlyCosts)
    printCosts(yearlyCosts, monthlyCosts)


def addCosts(a, b, c, d, e):
    monthlytotal = a + b + c + d + e
    return int(monthlytotal)

def calculateYearlyCost(monthlytotal):
    yearlyCost = monthlytotal * 12
    return yearlyCost

def printCosts(yearlyCost, monthlyCost):
    print("The monthly total for your vehicle is:", format(monthlyCost, ',.2f'))
    print("The yearly total for your vehicle is:", format(yearlyCost, ',.2f'))

main()
