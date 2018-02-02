import sys
import json

txtpath = sys.argv[1]
txtfile = open(txtpath, "r")
lines = txtfile.readlines()

jsonpath = txtpath + ".json"
jsonfile = open(jsonpath, "w")

data = {"perimeter":[]}
#data["perimeter"].append({"x":1, "y":2})

for line in lines:
    print(line)

print(data)
