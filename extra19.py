# defining the variables and the script
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a napkin.\n"

# connecting a new function to the script
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# connecting another function to the script
# using secondary variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amout_of_crackers = 50
# further defining variable names
cheese_and_crackers(amount_of_cheese, amout_of_crackers)

# using an equation to give variables a new number
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# using the numbers given to primary variable names
# and adding a new number to that number
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amout_of_crackers +1000)

# a new function
def pizza_and_beer(pizza_count, cases_of_beer):
	print "We have %d pizzas!" % pizza_count
	print "We have %d cases of beer!" cases_of_beer
	print "Can you PARTY!"
	print "Get a life."

print "Giving the function numbers directly:"
pizza_and_beer(8, 4)

print "Using the variables from the script:"
amount_of_pizza = 4
amount_of_beer = 25

pizza_and_beer(amount_of_pizza, amount_of_beer)

print "Doing math inside:"
pizza_and_beer(8 - 3, 12 + 6)

print "Combining the two, variables and math:"
pizza_and_beer(amount_of_pizza + 9, amount_of_beer * 12)