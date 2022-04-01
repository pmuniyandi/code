"""
The company MRPaul want to send a pdf report to their participants 
which password enabled. 

Your function to accept name, DOB (dd/mm/yyyy) and 
twelve digit account number. 

This function 
should generate password which contains first four letters of name, 
day number from DOB 
and last four letters from account number.


# Muniyandi
# 03/03/1972
# 123456789012

Password: muni039012

Maim program to get input from user
create a function will accept (name, dob, acno) {
    name[0:4] => name[:4]
    dob[0:2]  => dob[:2]
    acno[-4:] => acno[8:12]
}
"""
from passwordlib import *

name = input("Name ")
dob = input("dob ")
acno = input("acno ")

extractname = extractName(name)  # extract name four letter
extractdob = extractDob(dob)  # extract name day letter
extractacno = extractAcno(acno) # extract name last 4 letter

password = passwordGen(extractname,extractdob,extractacno)

print(password)