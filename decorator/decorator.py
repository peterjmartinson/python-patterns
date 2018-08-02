
class Value(object):
    def __init__(self):
        self.value = None

    def setValue(self, new_value):
        self.value = new_value

    def getValue(self):
        return self.value

class DecorateValue(object):
    def addFourToValue(self, value):
        return value + 4

grump = Value()
print(grump.getValue())

grump.setValue(20)
print(grump.getValue())


decorate = DecorateValue()

print(decorate.addFourToValue(grump.getValue()))
