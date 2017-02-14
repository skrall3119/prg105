def main():
    print("The minimum amount of insurance you should buy is: $" + format(calculateInsurance(getCost()), ',.2f'))

def getCost():
    cost = float(input("enter cost of building: "))
    return cost

def calculateInsurance(cost):
    insuranceCost = cost * .8
    return insuranceCost
main()
