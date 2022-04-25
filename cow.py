from csv import writer

out = writer(open("cow.csv", "a"))         #creating output file w mode always creat a new file
record = [] #empty record for single record
records = [] #empty record for multiple record

#Reading Cow detail start
flag = 'y'
gen = "female"
g = "f"
while flag.lower() == 'y'.lower():
    cow_id = input('Cow id? ')
    breed = input('Breed? ')
    dob = input('Bob (dd/mm/yy)? ')
    weight = input('Weight? ')
    color = input('Color? ')
    healthstatus = input('Health status? ')
    gender = input('Gender (Male/Female)? ')
    if (gender.upper() == gen.upper() or gender.upper() == g.upper()):
        milking = input('milking (y/n)? ')
        gestationperiod = input('Gestationperiod (y/n)? ')

    milking = input('Milking (y/n)? ')
    vaccinationschedule = input('Vaccination schedule (dd/mm/yy) ')
    #Reading Cow detail end

    #adding Cow detail into record start
    record.append(cow_id) 
    record.append(breed) 
    record.append(dob) 
    record.append(weight) 
    record.append(color) 
    record.append(gender) 
    if ((gender.upper() == gen.upper()) or (gender.upper() == 'f'.upper())):
        record.append(milking) 
        record.append(healthstatus) 
    record.append(gestationperiod) 
    record.append(vaccinationschedule) 
    
    records.append(record) # adding to recored
    #adding Cow detail into record end
    flag = input('continue (y/n)? ')
    record = [] # empty record object

for record in records: # write one by one using for loop
    out.writerow(record) # writing to output file