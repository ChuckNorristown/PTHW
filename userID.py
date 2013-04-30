#get name, no spaces
#get age, logical range
#get userID, 0-999999

from sys import argv
prompt = '>>>'

print "To sign in, please enter your username:"
username = raw_input(prompt) 
    
if len(username) > 20:
	print "Username must be no more than 20 characters.\n Please re-enter username:"
	
elif len(username) < 1:
	print "Username must be at least 1 character.\n Please re-enter username:"

else:
    print "Please enter your age:"

age = int(raw_input(prompt))
if age < 18:
   print "You need to come back in a few years, or lie.\n Please re-enter your age:"
  
elif age > 100:
	print "I think you might be a ghost.\n Please re-enter your age:"

else:
    print "Please enter your userID:"

userID = int(raw_input(prompt))

if userID < 0:
	print "UserID must be a positive number.\n Please re-enter your userID:"

elif userID > 999999:
	print "UserID must be less than 1 million.\n Please re-enter your userID:"

else:
	print """
	Your username is %r.
	Your age is %r.
	Your userID is %r.
	""" % (username, age, userID)






