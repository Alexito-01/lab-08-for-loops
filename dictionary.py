myData = {"effective top tube length": 515, "seat tube length": 500, "seat tube angle": 74.4, "head tube angle": 70.5, "stack": 513, "reach": 367, "standover height": 755}
for x, y in myData.items():
	print ("key: " + x, y)
print("ALL KEYS: ")
for x in myData:
	print (x)
print("ALL VALUES: ")
for x in myData.values():
	print (x)