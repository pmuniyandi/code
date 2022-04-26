
import pymongo
# connection string to connect into DB
#command to connect
spclient = pymongo.MongoClient(dbconnection)
#DB name
spdb = spclient["spfarm"]
#document or table for user
spuser = spdb["userdetail"]
#document or table for cow
spcow = spdb["cowdetail"]
#document or table for feed
spfeed = spdb["feeddetail"]
#document or table for expense
spexpense = spdb["expensedetail"]
#document or table for milking
spmilking = spdb["milkingdetail"]
#document or table for doctor visit
spdoctorvisit = spdb["doctorvisitdetail"]



