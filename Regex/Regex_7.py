import re

s = "purple alice@google.com acde helloab@abc.com ---@gmail.com 23@gmail.com my23@gmail.com _gmail.com \
    wel-come@gmail.com"
res = ["alice@google.com", "helloab@abc.com","my23@gmail.com","wel-come@gmail.com"]

# emails = re.findall(r"[a-z]*\d*-*@[a-z]+\.com", s)
# print(emails)

# emails = re.findall(r"\w+@\w+\.\w+",s)
# print(emails)

# emails = re.findall(r"[A-Za-z]\w+@\w+\.\w+",s)
# print(emails)

# emails = re.findall(r"[a-z]+\s(\w+@[a-z]+.com)", s)
# print("sol 1: ", emails)

# emails = re.findall(r"[a-z]+@[a-z]+\.com | \d+@[a-z]+\.com", s)
# print("sol 2: ", emails)

# gmailids=re.findall(r"[\w|\d|]+[\w|-]+.@g\w+.com",s)
# print(gmailids)

