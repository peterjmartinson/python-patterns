class Car(object):
  '''Resource intensive object'''
  def driveCar(self):
    print("Driving the car...")

class CarProxy(object):
  '''Less resource intensive object acting as a proxy.
  Instantiates the car object only if the driver is older than 18'''
  def __init__(self):
    self.ageOfDriver = 15
    self.car = None
  
  def driveCar(self):
    print("Proxy in action!  Checking to see if driver is of age...")

    if self.ageOfDriver >= 18:
      self.car = Car()
      self.car.driveCar()
    else:
      print("Driver is underage.")

carProxy = CarProxy()
carProxy.driveCar()

carProxy.ageOfDriver = 17
carProxy.driveCar()

carProxy.ageOfDriver = 18
carProxy.driveCar()
