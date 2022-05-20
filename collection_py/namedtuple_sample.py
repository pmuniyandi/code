from collections import namedtuple
a = namedtuple('courses' , 'name , tech')
s = a('data science' , 'python')
print(s.name)