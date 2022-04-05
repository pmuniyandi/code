'''7. Write a function to get numerology for your DOB, Add all the digit in DOB, if output is more then 
single digit repeat until become single digit (ex: 03/03/1972 => 0+3+0+3+1+9+7+2 => 25 => 2+5 => 7)
Main program should 
    a. Get DOB
    b. Call your function
    c. Display given DOB and numerology number 
    d. Call until you want to stop process.
'''
def addDigit(data):
    sum = 0
    for digit in data:
        sum += int(digit)
    
    return sum

def addDigitNumber(data):
    sum = 0
    
    while (data != 0):
        digit = data % 10  # extract last digit
        data = data // 10 # remove last digit
        sum += digit

    return sum


dob = input("Enter DOB (dd/mm/yyyy)") #enter dob
print(dob)
dob_list = dob.split("/")
print(dob_list)
print(int(dob_list[0]))

day_number = addDigitNumber(int(dob_list[0]))
month_number = addDigitNumber(int(dob_list[1]))
year_number = addDigitNumber(int(dob_list[2]))

print(day_number)
print(month_number)
print(year_number)
