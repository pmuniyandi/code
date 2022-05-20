from collections import deque


dq = deque([10, 20, 30])
lst = [40,20,30]
print(dq)
print(lst)
lst.sort()
print(lst)
dqs = deque("Muni")

dqs.extend("yandi")
print(dqs)