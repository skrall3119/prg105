def main(): #the main function that prints the lowest reccomended insurance payment.
    print("The minimum amount of insurance you should buy is: $" + format(calculateInsurance(getCost()), ',.2f'))

def getCost(): #gets the value of the building from the user
    cost = float(input("enter cost of building: "))
    return cost

def calculateInsurance(cost):# calculates the insurance cost using the value recieved from the user
    insuranceCost = cost * .8
    return insuranceCost
main()
