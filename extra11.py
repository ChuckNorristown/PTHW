print 30 * '-'
print "   MAIN-MENU"
print 30 * '-'
print "1. Backup"
print "2. User management"
print "3. Reboot the server"
print 30 * '-'

# get input
choice = raw_input('Enter your choice [1-3] : ')

choice = int(choice)

if choice == 1:
	print ("Starting backup...")
elif choice == 2:
	print ("Starting user management...")
elif choice ==3:
	print ("Rebooting the server...")
else:
	print ("Invalid entry. This computer will self destruct in 3... 2... 1...")