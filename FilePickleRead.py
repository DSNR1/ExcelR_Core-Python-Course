import pickle

fh = open("vdstates", "rb")
contents = pickle.load(fh)
fh.close()

print("file contents: ", contents)
print("Type of file contents, ", type(contents))
