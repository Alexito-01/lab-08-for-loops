print("Let's party...")
timer = input("How long 'til the party? ")
if (int(timer) > 0):
	for x in range(int(timer), 0, -1):
		print(x)
	print("PARTY TIME!!!")
else:
	print("PARTY NOW!!!")