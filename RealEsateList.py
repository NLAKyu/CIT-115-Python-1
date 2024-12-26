def getFloatInput(sPrompt):  # Convert user input to a Float / I used the float function i made from
                                                                 #my last assignment :D
    while True:
        try:
            userInput = float(input(sPrompt))
            if userInput <= 0:
                print("Input must be a number greater than 0.")
            else:
                return userInput
        except ValueError:
            print("Input must be a number greater than 0.")
            
def getMedian(fPrices):
    fPrices.sort()  # sorts the prices in order
    listLength = len(fPrices)

#if the number of elements is odd
    if listLength % 2 == 1:
        return fPrices[listLength // 2]  # Return the middle element

#or if the number of elements is even
    elif listLength % 2 == 0:
        middleIndex1 = listLength // 2 - 1  # element before the middle
        middleIndex2 = listLength // 2      #Element after the middle
        return (fPrices[middleIndex1] + fPrices[middleIndex2]) / 2  # average the two middle values

def main():
    salesValue = []  #List to store sales values
    propertyCount = 1

    while True:
        propertyPrice = getFloatInput("Enter property sales value: ")
# Add the property price to the list
        salesValue.append(propertyPrice)

# Ask the user if they want to enter another property
        while True:
            repeatInput = input("Enter another value Y or N: ").strip().lower()

            if repeatInput == 'y':
                propertyCount += 1  # Increment property count
                break
            elif repeatInput == 'n':
                break  
        if repeatInput == 'n':
            break  #Exit the loop when the user chooses n
#sort list
    salesValue.sort()
    propertyNumber = 1
    
    for element in salesValue:
        print(f"Property {propertyNumber} $   {element:,.2f}")
        propertyNumber += 1

#calcs        
    total = sum(salesValue)
    average = total / len(salesValue)
    min_value = min(salesValue)
    max_value = max(salesValue)
    median = getMedian(salesValue)
    commission = total * 0.03  # Commission is 3% of total sales

    print(f"Minimum:    $ {min_value:,.2f}")
    print(f"Maximum:    $ {max_value:,.2f}")
    print(f"Total:      $ {total:,.2f}")
    print(f"Average:    $ {average:,.2f}")
    print(f"Median:     $ {median:,.2f}")
    print(f"Commission: $ {commission:,.2f}")

main()
