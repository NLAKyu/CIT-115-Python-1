#Grade Analyzer HW

#Input for Name & Test Scores
sName = input("Name of person that we are calculating the grades for: ")
iTest1 = int(input("Test 1: "))
iTest2 = int(input("Test 2: "))
iTest3 = int(input("Test 3: "))
iTest4 = int(input("Test 4: "))
sDropGrade = input("Do you wish to Drop the Lowest Grade Y or N? ")

# Calculation & Output for a Score of 0 or Invalid value entered.
if iTest1 <= 0 or iTest2 <= 0 or iTest3 <= 0 or iTest4 <= 0:
    print("Test scores must be greater than 0")
    raise SystemExit

if sDropGrade != 'Y' and sDropGrade != 'N':
    print("Enter Y or N to Drop the Lowest Grade.")
    raise SystemExit

# Logic for dropping the lowest grade and calculating the average
if sDropGrade == 'Y':
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        flAverage = (iTest2 + iTest3 + iTest4) / 3
    elif iTest2 <= iTest1 and iTest2 <= iTest3 and iTest2 <= iTest4:
        flAverage = (iTest1 + iTest3 + iTest4) / 3
    elif iTest3 <= iTest1 and iTest3 <= iTest2 and iTest3 <= iTest4:
        flAverage = (iTest1 + iTest2 + iTest4) / 3
    else:  
        flAverage = (iTest1 + iTest2 + iTest3) / 3
elif sDropGrade == 'N':
    flAverage = (iTest1 + iTest2 + iTest3 + iTest4) / 4
    
#Determinating the Letter Grades        
if flAverage >= 97:
        sLetterGrade = 'A+'
elif 94.0 <= flAverage < 96.9:
        sLetterGrade = 'A'
elif 90.0 <= flAverage < 93.9:
        sLetterGrade = 'A-'
elif 87.0 <= flAverage < 89.9:
        sLetterGrade = 'B+'
elif 84.0 <= flAverage < 86.9:
        sLetterGrade = 'B'
elif 80.0 <= flAverage < 83.9:
        sLetterGrade = 'B-'
elif 77.0 <= flAverage < 79.9:
        sLetterGrade = 'C+'
elif 74.0 <= flAverage < 76.9:
        sLetterGrade = 'C'
elif 70.0 <= flAverage < 73.9:
        sLetterGrade = 'C-'
elif 67.0 <=flAverage < 69.9:
        sLetterGrade = 'D+'
elif 64.0 <=flAverage < 66.9:
        sLetterGrade = 'D'
elif 60.0 <=flAverage < 63.9:
        sLetterGrade = 'D-'
else: #59.9 or less
    sLetterGrade = 'F'

#Output for Test Average & Letter Grade    
print(f"{sName} test average is: {flAverage:.1f}")
print(f"Letter Grade for the test is: {sLetterGrade}")
