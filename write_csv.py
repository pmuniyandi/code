from csv import reader, writer # importing require lib
# data has all the record from a file in list
data = list(reader(open("Medicalpremium.csv", "r"))) # opening csv file

out = writer(open("output.csv", "w")) # output file
# record will have each record in a iteration
for record in data: # travel through all record in a list object which has all records
    height = int(record[1]) / 100 # reading height from single and conver to meter
    weight = int(record[2])  # reading weight from current
    hsqr  = height * height # height sqr
    bmi = weight / hsqr # bmi
    record.append(bmi) # adding bmi into same record
    #print(record) # right weight height - 100
    out.writerow(record) # writing to output file
  