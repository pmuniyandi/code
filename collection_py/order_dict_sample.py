import collections
#Create normal dict
my_dict = {}
my_dict['AA'] = 11
my_dict['BB'] = 22
my_dict['CC'] = 33
my_dict['DD'] = 44
for item in my_dict.items():
   print(item)
#Change the value for key BB
my_dict['BB'] = 100
print('After changing in Dict')
for item in my_dict.items():
   print(item)
print()
#Create ordered dict
my_ord_dict = collections.OrderedDict()
my_ord_dict['AA'] = 11
my_ord_dict['BB'] = 22
my_ord_dict['CC'] = 33
my_ord_dict['DD'] = 44
for item in my_ord_dict.items():
   print(item)
#Change the value for key BB
my_ord_dict['BB'] = 100
print('After changing in Ordered Dict')
for item in my_ord_dict.items():
   print(item)