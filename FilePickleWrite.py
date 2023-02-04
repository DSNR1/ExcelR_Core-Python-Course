import pickle

vaccine_details = {"Karnataka":{"Covi": 5, "Covax":2, "Sput":3, "Users":[1,2,3,4]},
"Maharastra":{"Covi": 6, "Covax":4, "Sput":3, "Users":[1,2,3]},
"Delhi":{"Covi": 5, "Covax":2, "Sput":3, "Users":[1,2]}}

fh = open("vdstates", "wb") #"wb" = Write + Binary
pickle.dump(vaccine_details, fh)
fh.close()