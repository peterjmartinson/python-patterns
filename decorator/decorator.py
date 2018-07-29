
class Value(object):
    def __init__(self):
        self.value = None

    def setValue(self, new_value):
        self.value = new_value

    def getValue(self):
        return self.value


grump = Value()
print(grump.getValue())

grump.setValue(20)
print(grump.getValue())
