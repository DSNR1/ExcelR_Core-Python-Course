fh = open("FileExample.txt","r")

s = fh.read()
fh.close()

print("File contents: ", s)