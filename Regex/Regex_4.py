import re

s = '''
<html>
<head>
<title>Current IP Address Allocations
</title>
</head>
<body>
IP Address are 172.45.78.109
LoopBack Address: 127.0.0.1
Computer 1: 10.67.89.101
Computer 2: 10.67.98.102
Computer 3: 12.68.98.102
</body>
</html>
'''
# Ip Address : 4 parts
# <no>.<no>.<no>.<no>
# \d

#lstValues = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", s)
# print(lstValues)

lstValues = re.findall(r"10.\d{1,3}\.\d{1,3}\.\d{1,3}", s)
print(lstValues)