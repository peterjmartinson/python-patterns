class Rapper(object):
    name = None
    likes = None
    def __init__(self, name):
        self.name = name
    def setInterests(self, interest): pass
    def talk(self): pass

class GoodRapper(Rapper):
    def setInterest(self, interest):
        self.likes = interest
    def talk(self):
        message = self.name + " likes " + self.likes
        print(message)

class EvilRapper(Rapper):
    def setInterest(self, interest):
        self.likes = interest
    def talk(self):
        message = self.name + " does not like " + self.likes
        print(message)



class Street(object):
    name = None
    quality = None
    def __init__(self, name):
        self.name = name
    def setDescription(self, quality): pass
    def describe(self): pass

class GoodStreet(Street):
    def setDescription(self, quality):
        self.quality = quality
    def describe(self):
        message = self.name + " Street welcomes you with " + self.quality
        print(message)

class BadStreet(Street):
    def setDescription(self, quality):
        self.quality = quality
    def describe(self):
        message = self.name + " Street repels you with " + self.quality
        print(message)



class Town(object):
    rapper = None
    street = None
    def setRapper(self, rapper_type):
        self.rapper = rapper_type
    def setStreet(self, street_type):
        self.street = street_type

class TownFactory(object):
    def getTown(self, town_type):
        town = Town()
        if town_type == 'good':
            town.setRapper(GoodRapper("Sir Mixalot"))
            town.rapper.setInterest("Big Butts")
            town.setStreet(GoodStreet("Helle"))
            town.street.setDescription("sunshine")
        elif town_type == 'bad':
            town.setRapper(EvilRapper("Sir Mixesalittle"))
            town.rapper.setInterest("Big Butts")
            town.setStreet(BadStreet("Dunkle"))
            town.street.setDescription("darkness")
        return town




factory = TownFactory()

good_town = factory.getTown('good')
bad_town = factory.getTown('bad')

good_town.rapper.talk()
good_town.street.describe()
bad_town.rapper.talk()
bad_town.street.describe()

