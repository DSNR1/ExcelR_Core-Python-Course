import re
# For a given list, filter all elements having a line starting with den or ending ly
items = ["lovely", "dentist", "2 lonely", "eden", "fly\nfar", "dent"]


result = []

for i in items:
    if re.search(r"^den|ly$", i):
        result.append(i)
print(result)