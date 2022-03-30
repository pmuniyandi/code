'''# different way to create list
list1 = []  # empty list object
list2 = list() # emptu
list3 = [10, 20, 20]  
list4 = list([100, 200, 200]) # 
#data = list(reader(open("Medicalpremium.csv", "r")))
# modify data
list1.append(1000)
list2.append(1)
list3[0] = 10.5 # modify data by location
print(list1, list2, list3, list4)

# remove data
print(list3.pop())
print(list3)
print(list4.remove(200))
print(list4)

# different way to create tuple
tuple1 = () 
tuple2 = tuple()
tuple3 = (10,20,20) 
tuple4 = tuple([100, 200])
# modify data
#tuple1.append(1000)
#tuple2.append(1)
#tuple3[0] = 10.5
print(tuple1, tuple2, tuple3, tuple4)
# remove data
#print(tuple3.pop())
print(tuple3)
#print(tuple4.remove(200))
print(tuple4)
'''
# different way to create set
set1 = {}
set2 = set()
set3 = {100, 10,20,30}
set4 = set({10,20,30,30,30})
# modify data
#set1.append(1000)
#set2.append(1)
#set3[0] = 10.5
print(set1, set2, set3, set4)
# remove data
#print(set3.pop())
#print(set3)
print(set4.remove(30))
#print(set4)



