from sys import argv

script, first_file_name = argv

first_file_contents = open(first_file_name)

print "Here's the file that you named on the command line :" 
print first_file_contents.read()

print "Type the name of a second file:"
second_file_name = raw_input("> ")

second_file_contents = open(second_file_name)

print second_file_contents.read()
first_file_contents.close()
second_file_contents.close()