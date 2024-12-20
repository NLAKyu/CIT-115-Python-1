#Compounding Interest HW
#This was difficult but fun, I like functions

#Non Zero or Negative input
def positiveFloat(sPrompt):
    while True:
        try:
            userInput = float(input(sPrompt))
            if userInput > 0:
                return userInput
            else:
                print("Input must be a positive numeric value")
        except ValueError:
          print("Input must be a positive numeric value")
#Zero is allowed for input but not negatives.
def nonNegativeNumb(sPrompt):
    while True:
        try:
            userInput = float(input(sPrompt))
            if userInput >= 0:
                return userInput
            else:
                print("Input must be 0 or greater")
        except ValueError:
            print("Input must be a positive numeric value")

def compoundInterest():
    # get user inputs
    originalDeposit = positiveFloat("What is the Original Deposit (positive value): ")
    interestRate = positiveFloat("What is the Interest Rate (positive percentage): ")
    totalOfMonths = int(positiveFloat("What is the Number of Months (positive value): "))
    goalAmount = nonNegativeNumb("What is the Goal Amount (can enter 0 but not negative: ")

    #Calculate monthly interest rate
    monthlyInterest = (interestRate / 100) / 12

    currentBalance = originalDeposit
    for iMonths in range(1, totalOfMonths + 1):
        earnedInterest = currentBalance * monthlyInterest
        currentBalance += earnedInterest
        print(f"Month: {iMonths} Account Balance is: ${currentBalance:,.2f}")

    #how many months it will take to reach the goal
    if goalAmount> 0:
        monthsGoal = totalOfMonths
        while currentBalance < goalAmount:
            earnedInterest = currentBalance * monthlyInterest
            currentBalance += earnedInterest
            monthsGoal += 1
        print(f"It will take {monthsGoal} months to reach your goal of ${goalAmount:,.2f}.")


def main():
    compoundInterest()
main()
