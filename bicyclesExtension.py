class Frame(object):
  def __init__(self, material, weight, cost):
    self.material = material
    self.weight = weight
    self.cost = cost
    
  def __repr__(self):
    template = "{0}, Weight: {1}lbs, Cost: ${2}"
    return template.format(self.material, self.weight, self.cost)


class Wheel(object):
  def __init__(self, model, weight, cost):
    self.model = model
    self.weight = weight
    self.cost = cost
    
  def __repr__(self):
    template = "{0}, Weight: {1}lbs, Cost: ${2}"
    return template.format(self.model, self.weight, self.cost)
    
    
class Bicycle(object):
  def __init__(self, name, frame, wheel):
    self.name = name
    self.frame = frame
    self.wheel = wheel
    self.weight = frame.weight + (wheel.weight * 2)
    self.cost = frame.cost + (wheel.cost * 2)
  
  def __repr__(self):
    template = "{0}\n | Frame: {1}\n | Wheel: {2}\n | Total Weight: {3}lbs, Total Cost: ${4}"
    return template.format(self.name, self.frame, self.wheel, self.weight, self.cost)
  
  
class BikeShop(object):
  def __init__(self, name, margin, bikes):
    self.name = name
    self.margin = margin
    self.profit = 0
    self.inventory = {}
    
    for bike in bikes:
      bike.markup = bike.cost * (self.margin / 100.0)
      bike.price = bike.cost + bike.markup
      self.inventory[bike.name] = bike

  def __repr__(self):    
    bikes = "\n".join(str(bike) for bike in self.inventory.values())
    template = "\n{0} (Profit: ${1})\n\nBicycles Inventory:\n{2}\n"
    return template.format(self.name, "%.2f" % self.profit, bikes)
  
  def filter(self, budget):
    bikes = self.inventory.values()
    return [bike for bike in bikes if bike.price <= budget]
  
  def sell(self, bike, customer):
    customer.bike = bike
    customer.fund -= bike.price
    self.profit += bike.markup
    del self.inventory[bike.name]

    
class Customer(object):
  def __init__(self, name, fund):
    self.name = name
    self.fund = fund
    self.bike = None
