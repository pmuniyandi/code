def removeOdd(number):
    oddstr = "" # to store as string
    oddno = 0 # to store as int
    for digit in str(number):  # convert as string and getting char by char
    #print(digit) 
        if(int(digit) % 2) == 0: 
            oddstr += str(digit)# "2" => "24"
    oddno = int(oddstr)
    return oddno

def removeEven(number):
    evenstr = "" # to store as string
    evenno = 0 # to store as int
    for digit in str(number):  # convert as string and getting char by char
    #print(digit) 
        if(int(digit) % 2) != 0: 
            evenstr += str(digit)# "2" => "24"
    evenno = int(evenstr)
    return evenno

'''
1. Write a function to remove all odd digit from given number.  (ex: 7894 => 84)
Main program should 
     a. Get number
     b. Call your function
     c. Display given and modified number 
     d. Call until you want to stop process. 
'''

flag = 'y'
while flag == 'y' or flag == 'Y':
    number = int(input("Enter the number: ")) # getting input as int
    evenDigit = removeOdd(number) # convert using my function
    oddDigit = removeEven(number) # # convert using my function
    # reverse digit
    # sum data birth 
    # binary
    # octal
    # addition of digits
    print("Given #", number) # given number
    print("Modified (only even digit) #", evenDigit) # modifed 
    print("Modified (only odd) #", oddDigit) # nofi
    flag = input("Are you want to continue")




