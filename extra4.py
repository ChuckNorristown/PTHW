# in line 7 "car_pool _capacity" should be defined as "carpool_capacity"
# more extra credit
# 4.0 is used to get a more accurate number
# floating point allows for decimals

# number of "cars"
cars = 100
# max passengers per car
space_in_a_car = 4.0
# total "drivers"
drivers = 30
# "passengers" for the day
passengers = 90
# cars that won't be needed for the day (100 "cars" - 30 "drivers" = "cars not driven"=70)
cars_not_driven = cars - drivers
# "cars driven" will be the number of "drivers" for the day
cars_driven = drivers
# "cars driven"=30 (multiplied*by) "space in a car"=4.0 equals= "carpool capacity=120.0"
carpool_capacity = cars_driven * space_in_a_car
# "passengers"=90 (divided/by) "cars driven=drivers=30" equals= "average passengers per car=3"
average_passengers_per_car = passengers / cars_driven

# a new calculator
egg = 1
eggs_in_a_carton = egg * 12
omlette = egg * 3
eggs_left = eggs_in_a_carton - omlette
#making an omlette
print "There are", eggs_in_a_carton, "eggs in a carton."
print "I used", omlette, "eggs to make an omlette."
print "I have", eggs_left, "eggs left in my carton."
