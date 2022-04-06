## BMI Calculation for participant

For calculating BMI

- Need to get height (kg) and weight (cm)
- BMI calculation formula
- BMI = weight / height (meter) ^ 2

For this program, we are reading data from csv almost 1000 record
That record contain, age, height and weight with comma separated

Sample data from that Medicalpremium.csv file
- 45,155,57
- 60,180,73
- 36,158,59

Code to read from medical file - Medicalpremium.csv which is there in same folder where python code is running. 

```
from csv import reader, writer # importing require lib
data = list(reader(open("Medicalpremium.csv", "r"))) # opening csv file
```
Data will hold all the record from Medicalpremium.csv. 
Following steps and logic will 
- extract record by record  
- parse age, height and weight
- convert from cm to age
- call function to calculate BMI -> def bmiCalculator(height, weight):
- call function to health status -> def healthStatus(bmi):
- call function to find right weight -> def rightWeight(height):
- call function to flag of correct weight or not -> def weightFlag(weight, right_weight):
- write into output.csv file contain all new column

Sample record from that output.csv file
45,155,57
60,180,73
36,158,59

### output.csv
```
out = writer(open("output.csv", "w")) # output file
out.writerow(record) # writing to output file
```
### bmiCalculator(height, weight)
```
# Calculating bmi using height/weight
def bmiCalculator(height, weight):
    height_m = height / 100 # reading weight from current
    hsqr  = height_m * height_m # height sqr  
    bmi = weight / hsqr # bmi
    bmi = round(bmi, 2) # lib/predefined function
    return bmi
```
### healthStatus(bmi)
```
# Calculating Health status by bmi
'''
Severe Thinness< 16 -3
Moderate Thinness16 - 17 - 2
Mild Thinness17 - 18.5 -1 
Normal18.5 - 25 0
Overweight25 - 30 1
Obese Class I30 - 35 2
Obese Class II35 - 40 3
'''
def healthStatus(bmi):
    health_status = 0
    if (bmi < 16):
        health_status = -3
    if (bmi >= 16 and bmi > 17):
        health_status = -2
    if (bmi >= 17 and bmi > 18.5):
        health_status = -1
    if (bmi >= 18.5 and bmi > 25):
        health_status = 0
    if (bmi >= 25 and bmi < 30):
        health_status = 1  
    if (bmi >= 30 and bmi < 35):
        health_status = 2
    if (bmi >= 35):
        health_status = 3
    return health_status
```
###rightWeight(height)
```
# Calculating right weight using height
def rightWeight(height):
    right_weight = height - 100
    return right_weight
```
###weightFlag(weight, right_weight)
```
# Calculating right flag
def weightFlag(weight, right_weight):
    weight_flag = 1
    if (weight > right_weight):
        weight_flag = 0
    return weight_flag
```
### repeating the steps for all record
```
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
 ```
 
 
### Support 
Having trouble ? Check out 
- [All function](https://github.com/pmuniyandi/code/blob/master/healthcalculator.py).
- [Main program to read/write](https://github.com/pmuniyandi/code/blob/master/write_csv.py).
- [Medicalpremium.csv](https://raw.githubusercontent.com/pmuniyandi/code/master/Medicalpremium.csv).

