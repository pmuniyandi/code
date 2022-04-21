from csv import writer

out = writer(open("cow.csv", "w"))         #creating output file
record = [] #empty record for single record
records = [] #empty record for multiple record

#Reading Cow detail start
flag = 'y'
while flag == 'y' or flag == 'Y':
    cow_id = input('cow id? ')
    breed = input('breed? ')
    dob = input('dob (dd/mm/yy)? ')
    weight = input('weight? ')
    color = input('color? ')
    milking = input('milking (y/n)? ')
    healthstatus = input('health status? ')
    gestationperiod = input('gestationperiod (y/n)? ')
    vaccinationschedule = input('vaccination schedule (dd/mm/yy) ')
    #Reading Cow detail end

    #adding Cow detail into record start
    record.append(cow_id) 
    record.append(breed) 
    record.append(dob) 
    record.append(weight) 
    record.append(color) 
    record.append(milking) 
    record.append(healthstatus) 
    record.append(gestationperiod) 
    record.append(vaccinationschedule) 
    
    records.append(record) # adding to recored
    #adding Cow detail into record end
    flag = input('continue (y/n)? ')


out.writerow(records) # writing to output file