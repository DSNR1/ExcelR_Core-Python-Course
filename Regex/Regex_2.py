import re
s = "Welcome to Regex     Programming    using Python"
#s = "Welcome to Regex 8Programming using9 Python0 #, "
lstValues = re.split(r"\s", s)
print("Regex split using \s                     :", lstValues)

lstValues = re.split(r"\s+", s)
print("Regex split using \s+                     :", lstValues) #split one or more spaces

lstValues = re.split(r"s+", s)
print("Regex split using s+                     :", lstValues) # split by s

s = "Welcome to Regex Programming using Python"
lstValues = re.split(r"[a-f]", s)
print("Regex split using [a-f]                     :", lstValues) 

s = "Welcome to Regex Programming using Python"
lstValues = re.split(r"[a-f][l-n]", s)
print("Regex split using [a-f][l-n]                   :", lstValues)