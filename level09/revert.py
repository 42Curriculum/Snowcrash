import sys

file = sys.argv[1]
i =0
while file[i]:
	sys.stdout.write(chr(ord(file[i])-i))
	sys.stdout.flush()