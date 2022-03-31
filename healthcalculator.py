# Calculating bmi using height/weight
def bmiCalculator(height, weight):
    height_m = height / 100 # reading weight from current
    hsqr  = height_m * height_m # height sqr  
    bmi = weight / hsqr # bmi
    bmi = round(bmi, 2) # lib/predefined function
    return bmi

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

# Calculating right weight using height
def rightWeight(height):
    right_weight = height - 100
    return right_weight

# Calculating right flag
def weightFlag(weight, right_weight):
    weight_flag = 1
    if (weight > right_weight):
        weight_flag = 0
    return weight_flag
