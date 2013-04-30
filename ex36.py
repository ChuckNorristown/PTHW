
print "Hey buddy, glad you decided to go on this trip with us."
print "Before we go we're gonna need you to grab some supplies."
print "The only problem is, I can't tell you what we need."
print "You'll have to figure out on your own,\nbut I'll let you know if you get the right things."
print "Sorry, I'm horrible with names. Do you mind\ntelling me your first name again?"

name = raw_input('>>> ').lower()

print "Oh yeah, how could I forget!"
print "Ok %r, what have you decided to bring?" % (name)

bring = raw_input('>>> ').lower()

if name[0] == bring[0]:
    print "Perfect! that's just what we needed."

elif name[0] != bring[0]: 
    print "Why the hell would you bring that!? Try bringing something useful."
    raw_input('>>> ').lower()

else:
    print "Thanks but no thanks, we're leaving without you."





