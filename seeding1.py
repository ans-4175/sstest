import sys
#seeding_files
from random import randint
with open(sys.argv[1], "ab") as myfile:
	for num in range(0,int(sys.argv[2])):
		rand = randint(0,63)
		print rand
		myfile.write(str(rand))
		myfile.write("\n")