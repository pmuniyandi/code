## Destiny,  Day number calculation using Date of Birth [Video](https://youtu.be/a7lAki-vsHU)

For calculating Day number, Destiny number from Date of brith. (ex: 03/03/1972 => 0+3+0+3+1+9+7+2 => 25 => 2+5 => 7)

Step 1: Split DD, MM, & YYYY from Date of Birth. 

If you are getting your DOB from user, it will always come as string. Split as list from given string using split string function using "/" as separator.

 ```
 dob = input("DOB (dd/mm/yyyy) ") # getting DOB as string
 dob_array = dob.split("/") # spliting as three element list as date, month and year
 ```
 
 Write a user defined function to calculate single digit from given number
 
 ```
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
 ```

Write calling program to get DOB and split in list
- Get DOB
- Split into DD, MM, YYYY
- Convert as integer of DD, MM, YYYY
- Sum DD + MM + YYYY
- Call sumDigit function

```
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
```
## Numerology calculation for name

Declare dictionary for numeroloy value for all charactor a-z

Write function to split charactor from name and calculate numerology number for name.
```
def nameNumber(name):
    sum = 0
    namedic = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':8,'g':3,'h':5,'i':1, 'j':1,'k':2,
                'l':1,'m':4,'n':5,'o':7,'p':8,'q':1,'r':2,'s':3,'t':4,'u':6,'v':6,
                'w':6,'x':5, 'y':1,'z':7}
    for namechar in name:
        namechar = namechar.lower()
        sum += namedic[namechar]

    return sum
 ```
 Write calling program to 
- Get name
- Call nameNumber function find number for given name
- Call sumDigit(<namenumber>) to convert as single digit
  
```
name = input("Name ")
print("Name ", sumDigit(nameNumber(name)))
```
### Support 
Having trouble ? Check out [Git Code](https://github.com/pmuniyandi/code/blob/master/numerology.py) 
