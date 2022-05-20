from collections import Counter
name1 = "Muniyandi"
cntr1 = Counter()
for name_char in name1:
    cntr1[name_char] += 1

name2 = "Sumathi"
cntr2 = Counter()
for name_char in name2:
    cntr2[name_char] += 1

print(cntr1)
print(cntr1["u"])
print(cntr1.elements())

for element in cntr1.elements():
    print(element)

print(cntr1.most_common(10))


print(cntr1.subtract(cntr2))

