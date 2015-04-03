import random
from bicyclesExtension import *

frames = [
  Frame("Aluminum", 10, 100), 
  Frame("Steel", 30, 500)
]


wheels = [
  Wheel("26inch / ISO 559mm", 2, 20), 
  Wheel("27.5inch / ISO 584mm", 3, 40), 
  Wheel("29inch / ISO 622mm", 5, 60)
]


bikes = [
  Bicycle("Wind Ranger", frames[0], wheels[0]),
  Bicycle("Shadow Striker", frames[0], wheels[1]),
  Bicycle("Storm Spirit", frames[0], wheels[2]),
  Bicycle("Fire Dancer", frames[1], wheels[0]),
  Bicycle("Water Morpher", frames[1], wheels[1]),
  Bicycle("Earth Shaker", frames[1], wheels[2])
]


shop = BikeShop("Elemental Cycles", 20, bikes)


customers = [
  Customer("Leonardo", 200), 
  Customer("Michaelangelo", 500), 
  Customer("Donatello", 800), 
  Customer("Raphael", 1000)
]


print shop


print "Customers:"
for customer in customers:
  bikes = ", ".join(bike.name for bike in shop.filter(customer.fund))
  print customer.name + " (Budget: $" + str(customer.fund) + ")\n | " + "Affordable Bicycles: " + bikes
print ""

template = "{0} bought the {1} at ${2} and he/she has ${3} remainder."


for customer in customers:
  afford = shop.filter(customer.fund)
  shop.sell(random.choice(afford), customer)
  
  print template.format(
    customer.name, customer.bike.name,
    int(customer.bike.price), int(customer.fund)
    )

  
print shop