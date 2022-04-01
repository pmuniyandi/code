def passwordGen(name, dob, acno):
    return name+dob+acno

def extractName(name):  # muniyandi perumal
    ns = name.split() # ns[0] => muniyandi ns[1] => perumal
    return ns[0][:4]

def extractDob(dob):
    return dob[-4:]

def extractAcno(acno):
    return acno[-4:]
