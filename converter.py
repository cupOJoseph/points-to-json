import sys
import json

#use: $ python3 converter.py sample.txt
#will create sample.txt.json

txtpath = sys.argv[1]
txtfile = open(txtpath, "r")
lines = txtfile.readlines()

data = {"perimeter":[]}
#data["perimeter"].append({"x":1, "y":2})

for line in lines:
    x,y = line.split(",")

    #remove '(' and ')\n'
    x = x[1:]
    y = y[:-2]

    #add to
    data["perimeter"].append({"x":float(x), "y":float(y)})


jsonpath = txtpath + ".json"
jsonfile = open(jsonpath, "w")
json.dump(data, jsonfile)
