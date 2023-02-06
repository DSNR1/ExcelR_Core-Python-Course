# Pattern Object

import re

s1 = "creed refuse removed read"
s2 = "refused reed redo recieved"

print(re.findall(r"re(mov|ciev|fus)ed", s2))
pat = re.compile(r"re(mov|ciev|fus|)ed")

print(re.sub(pat,"X",s1))
print(re.sub(pat,"X",s2))