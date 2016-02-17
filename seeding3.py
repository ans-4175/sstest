import sys
#seeding_files
import random
import string

def rand_name(length):
    rand_str = ''.join(random.choice(string.ascii_lowercase)
    			for i in range(length))
    return rand_str

def rand_phone(length):
    rand_str = ''.join(random.choice(string.digits)
    			for i in range(length))
    return rand_str

with open(sys.argv[1], "ab") as myfile:
	for num in range(0,int(sys.argv[2])):
		name = rand_name(5)
		phoneno = rand_phone(5)
		print ' '.join([name,phoneno])
		myfile.write(' '.join([name,phoneno]))
		myfile.write("\n")