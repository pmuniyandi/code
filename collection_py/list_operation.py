lst = {10, 20,-1,10}
print(lst.add(30))
lst1 = lst
lst.discard(10)
lst.pop()
print(len(lst), lst, [10,20,30].index())
print(len(lst1), lst1)
lst.clear()
print(len(lst), lst)
print(len(lst1), lst1)

print(lst.keys)