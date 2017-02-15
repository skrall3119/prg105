def main():
    actualValue = getValue()
    assessmentValue = calculateAssessmentValue(actualValue)
    propertyTax = findPropertyTax(assessmentValue)

    print("The assessment value of your home is: $" + format(assessmentValue, ',.2f'))
    print("The property tax on your home is: $" + format(propertyTax, ',.2f'))

def getValue():
    actualValue = float(input("Enter the actual value of your property. "))
    return actualValue

def calculateAssessmentValue(houseValue):
    assessmentValue = houseValue * .6
    return assessmentValue

def findPropertyTax(assessmentValue):
    x =  assessmentValue / 100
    propertyTax = .72 * x
    return propertyTax

main()
