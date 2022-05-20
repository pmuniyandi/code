from collections import defaultdict


#sample_dict = {}
#print(sample_dict["a"])
def def_value():
    return "No found"

sample_def_dict = defaultdict(def_value)
print(sample_def_dict["a"])
