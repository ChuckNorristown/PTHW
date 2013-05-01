def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None

num_to_test = raw_input("Give me something to test: ")
converted_num = convert_number(num_to_test)
print "The convert_number says: ", converted_num
