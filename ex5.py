name = 'Sean P. Shields'
age = 33 # not a lie
height = 69 # inches
weight = 170 # lbs
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'
height_in_cm = 1 * 2.54
weight_in_kilo = 1 * .453592

print "Let's talk about %s." % name
print "He's %d inces tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffe." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + (height * 2.54) + (weight * .453592)) 