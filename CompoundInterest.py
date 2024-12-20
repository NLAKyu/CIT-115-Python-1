#Compound Interest HW

#1.Input/Conversion

fPrincipalValue = float(input("Enter the starting principal: ")) # (PV)
fAnnualRate = float(input("Enter the annual interest rate: ")) # Divide by 100 to get (r)
nCompound = int(input("How many times per year is the interest compounded? ")) # (m)
nGrowthYears = int(input("For how many years will the account earn interest? ")) # (t)

#2.Calculations - Formula : PV * (1 + r / m) ** (m*t) 

nInterestRate = fAnnualRate / 100 # (r)
nFutureValue = fPrincipalValue * (1 + nInterestRate / nCompound) ** (nCompound * nGrowthYears) #(FV)

#3.Output - The calculated investment

print(f"At the end of {nGrowthYears} years you will have $ {nFutureValue:,.2f}")
