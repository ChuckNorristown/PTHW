from sys import exit

def idiot():
    print "Thought you were sooo slick."
    print "Turns out the wallet belonged to a cop!"
    print "After a brief investigation, the cop tracks you down at a...\nwe'll just call it an 'Adult Store'."
    print "You're later booked on felony identity theft charges."
    exit(0)

def lowlife():
    print "So you decided to take the cash, I hope you're proud of yourself."
    print "Well, between the cash and credit cards, you've netted about $8000."
    print "What do you plan on doing with your new found wealth?."

    next = raw_input(">>> ").lower(), slice()

    if next == "donate":
        print "Maybe you aren't the slimeball I thought you were."
    elif next == "return":
        good_samaritan()
    elif next == "shopping spree": 
        idiot()
    else:
        print "Stop dilly-dallying. A couple of street toughs are eyeing you up."


def good_samaritan():
    print "You should be proud of yourself."
    print "You did the right thing and returned the money back to it's rightful owner."
    print "Ohh but wait... it seems your good deed has not gone unnoticed."
    print "Looks like you got yourself a big fat $100 bill!"
    print "Do you kindly decline the offer, or politely say ,'Thank you' and go on about your buisness?"
    print "'decline' or 'accept'"

    next = raw_input(">>> ").lower(), slice()

    if "decline" in next:
        decline()
    elif "accept" in next:
        dead("Well that was tasty!")
    else:
        print "Give yourself a pat on the back"


def decline():
    print "So modest. Because of that kind gesture, your reward grew a just little bit."
    print "That $100 dollar reward you so gracefully declined just got bumped up to $500!"
    print "You probably used to rewind your video tapes before you returned them too."
    exit(0)

def start():
    print"You're walking down the street and discover a wallet on the ground."
    print "No one is around and you decide to pick up the wallet."
    print "You then open the wallet to find a very large sum of cash,\nas well as multiple credit cards\nalong with all of the owners personal info."
    print "Do you take the money and run, or return the wallet intact."
    print "'take' or 'return'"

    next = raw_input(">>> ").lower(), slice()

    if next == "take":
        lowlife()
    elif next == "return":
        good_samaritan()
    else:
        print "A prowler who was lurking in the bushes nearby, stabbed you and took the wallet."


start()