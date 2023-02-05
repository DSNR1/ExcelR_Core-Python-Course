import re
address = "78, hi 11     89 Main, 4th Cross, 123, Road, Marthalli, 5678 Bangalore, 560023, 67893 45"

# lstValues = re.findall(r"\d", address)
# print(lstValues)

# lstValues = re.findall(r"\d+", address)
# print(lstValues)
# lstValues_1 = re.findall(r"\d+", address)
# print(lstValues_1)
lstValues = re.findall(r"\d{6}", address)
print(lstValues)

lstValues = re.findall(r"\s\d{2}\s",address)
print(lstValues)

lstValues = re.findall(r"^\d{2}",address)
print(lstValues)
print("----------------")
lstValues = re.findall(r"\d{1,6}",address)
print(lstValues)
print("----------------")