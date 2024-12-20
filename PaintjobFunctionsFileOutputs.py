#Paintjob with funcs and output file HW
#I love functions 
import math

def getFloatInput(sPrompt):  # Convert user input to a Float
    while True:
        try:
            userInput = float(input(sPrompt))
            if userInput <= 0:
                print("Please enter a value greater than 0")
            else:
                return userInput
        except ValueError:
            print("Please enter a valid numerical value")

def getGallonsOfPaint(sqftOfWall, ftPerGallon):
    paintGallons = sqftOfWall / ftPerGallon
    return math.ceil(paintGallons)  # rounds up for whole gallons

def getLaborHours(hrsPerGallon, gallonTotals):
    return hrsPerGallon * gallonTotals

def getLaborCosts(laborHours, laborCost):
    return laborHours * laborCost

def getPaintCost(gallonTotals, paintCost):
    return gallonTotals * paintCost

def getSalesTax(customerState):
    if customerState == "CT":
        return 0.06
    elif customerState == "MA":
        return 0.0625
    elif customerState == "ME":
        return 0.085
    elif customerState == "NH":
        return 0.0
    elif customerState == "RI":
        return 0.07
    elif customerState == "VT":
        return 0.06
    else:
        return 0.0

# This function will display all calculated values to the screen
def showCostEstimate(lastName, gallonTotals, laborHours, paintCost, laborCost, salesTax, totalCost, taxedTotal):
    print(f"Gallons of paint: {gallonTotals}")
    print(f"Hours of labor: {laborHours:,.1f}") 
    print(f"Paint charges: ${paintCost:,.2f}") 
    print(f"Labor charges: ${laborCost:,.2f}")  
    print(f"Tax: ${salesTax * totalCost:,.2f}")  
    print(f"Total cost: ${taxedTotal:,.2f}")  

def main():
    # Inputs for Variables
    sqftOfWall = getFloatInput("Enter wall space in square feet: ")
    priceOfPaint = getFloatInput("Enter paint price per gallon: ")
    ftPerGallon = getFloatInput("Enter feet per gallon: ")
    hrsPerGallon = getFloatInput("How many labor hours per gallon: ")
    laborRate = getFloatInput("Labor charge per hour: ")

    #Inputs for the state and customer's last name
    customerState = input("State job is in: ")
    lastName = input("Customer Last name: ")

    #Calculations
    gallonTotals = getGallonsOfPaint(sqftOfWall, ftPerGallon)
    laborHours = getLaborHours(hrsPerGallon, gallonTotals)
    laborCost = getLaborCosts(laborHours, laborRate)
    paintCost = getPaintCost(gallonTotals, priceOfPaint)
    salesTax = getSalesTax(customerState)

    # Calculated total cost and tax
    totalCost = paintCost + laborCost
    taxAmount = totalCost * salesTax
    taxedTotal = totalCost + taxAmount

    #Cost estimate output to the screen
    showCostEstimate(lastName, gallonTotals, laborHours, paintCost, laborCost, salesTax, totalCost, taxedTotal)

    #file name using lastName
    fileName = f"{lastName}_PaintJobOutput.txt"

    # Write the output to a file
    with open(fileName, "w") as file:
        file.write(f"Gallons of paint: {gallonTotals}")
        file.write(f"Hours of labor: {laborHours:,.1f}")  
        file.write(f"Paint charges: ${paintCost:,.2f}")  
        file.write(f"Labor charges: ${laborCost:,.2f}")  
        file.write(f"Tax: ${salesTax * totalCost:,.2f}") 
        file.write(f"Total cost: ${taxedTotal:,.2f}")  

    print(f"File: {fileName} was created.")
    
main()


