from csv import reader, writer # importing require lib
from healthcalculator import *
# data has all the record from a file in list

data = list(reader(open("Medicalpremium.csv", "r"))) # opening csv file

out = writer(open("output.csv", "w")) # output file
# record will have each record in a iteration


# repeating the steps for all record
for record in data: # travel through all record in a list object which has all records
    height = int(record[1])  # reading height from single and conver to meter
    weight = int(record[2])
    
    bmi = bmiCalculator(height, weight) # user define 
    health_status = healthStatus(bmi) # health status c
    right_weight = rightWeight(height) # right wight
    weight_flag = weightFlag(weight, right_weight) # weight flag
 
    record.append(bmi) # adding bmi into same record
    record.append(right_weight) # adding bmi into same record
    record.append(weight_flag) # adding bmi into same record
    record.append(health_status) # adding bmi into same record

    #print(record) # right weight height - 100
    out.writerow(record) # writing to output file
  