from sys import argv
from os.path import exists

script, from_file = argv

print "Copying from %s to %s" % (from_file, to_file)

input = open(from_file)
indata = input.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist"