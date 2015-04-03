import random
from bicycles import Customer, Bicycle, BikeShop


bikes = [
  Bicycle("Earth Shaker", 40, 620), Bicycle("Fire Dancer", 34, 540), 
  Bicycle("Wind Ranger", 14, 140), Bicycle("Water Morpher", 36, 580), 
  Bicycle("Storm Spirit", 20, 220), Bicycle("Shadow Striker", 16, 180)
]

shop = BikeShop("Elemental Cycles", 20, bikes)

customers = [
  Customer("Snap", 200), Customer("Crackle", 500), Customer("Pop", 1000)
]

for customer in customers:
  bikes = ", ".join(bike.model for bike in shop.filter(customer.fund))
  print customer.name + " | " + "Affordable Bicycles: " + bikes

print shop

template = "{0} bought the {1} at ${2} and he/she has ${3} remainder."

for customer in customers:
  afford = shop.filter(customer.fund)
  shop.sell(random.choice(afford), customer)
  
  print template.format(
    customer.name, customer.bike.model,
    customer.bike.price, customer.fund
    )

print shop