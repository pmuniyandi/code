'''7. Write a function to get numerology for your DOB, Add all the digit in DOB, if output is more then 
single digit repeat until become single digit (ex: 03/03/1972 => 0+3+0+3+1+9+7+2 => 25 => 2+5 => 7)
Main program should 
    a. Get DOB
    b. Call your function
    c. Display given DOB and numerology number 
    d. Call until you want to stop process.

    1 -> A, I, J, Q, Y
    2 -> B, K, R
    3 -> C, G, L, S
    4 -> D, M, T
    5 -> E, H, N, X
    6 -> U, V, W
    7 -> O, Z
    8 -> F, P
'''
def nameNumber(name):
    sum = 0
    namedic = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':8,'g':3,'h':5,'i':1, 'j':1,'k':2,
                'l':1,'m':4,'n':5,'o':7,'p':8,'q':1,'r':2,'s':3,'t':4,'u':6,'v':6,
                'w':6,'x':5, 'y':1,'z':7}
    for namechar in name:
        namechar = namechar.lower()
        sum += namedic[namechar]

    return sum

def sumDigit(number):
    number = abs(number)
    sum = 0 # to store sum of digits
    while(number > 0 or sum > 9): # number > 0 or sum > 9
        if(number == 0): 
            number = sum
            sum = 0
        sum += number % 10
        number = number // 10
    return sum


dob = input("DOB (dd/mm/yyyy) ")
name = input("Name ")
dob_array = dob.split("/")

dd = int(dob_array[0])
mm = int(dob_array[1])
yyyy = int(dob_array[2])

dd_number = sumDigit(dd)
mm_number = sumDigit(mm)
yyyy_number = sumDigit(yyyy)

all_digit  = dd_number + mm_number + yyyy_number

destiny_num = sumDigit(all_digit)
day_num = sumDigit(dd_number)

print("Destiny number ", destiny_num)
print("Day number ", day_num)
print("Name ", sumDigit(nameNumber(name)))
