from sys import argv
from os.path import exists

script, Jay.txt, ex15_sample.txt = argv

print "Copying from %s to %s" % (jay.txt, ex15_sample.txt)

input = open(Jay.txt)
indata = input.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exist(ex15_sample.txt)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

output = open(ex15_sample.txt, 'w')
output.write(indata)

print "Alright, all done."

output.close()
input.close()

