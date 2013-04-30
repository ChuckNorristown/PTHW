# x = There are "10" types of people.
x = "There are %d types of people." % 10
# binary represents binary
binary = "binary"
# do_not represents don't
do_not = "don't"
# y = "Those who know binary and those who don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# print x print y = There are "10" types of people. -->
# Those who know binary and those who don't.
print x 
print y
# will display I said: There are 10 types of people.
print "I said: %r." % x
# will display I also said:'Those who know binary and those who don't.'
print "I also said: '%s'." % y
# hilarious represents false
hilarious = False
# joke_evaluation represents Isn't that joke so funny?! False
joke_evaluation = "Isn't that joke so funny?! %r"
# w represents This is the left side of...
w = "This is the left side of..."
# e represents a string with a right side
e = "a string with a right side."
# will display w and e as one statement
print w + e