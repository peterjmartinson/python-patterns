# The superclass
class binary_operation(object):
    def operate(self, x, y):
        """Run a binary operation and return the result"""
        pass


# The four subclasses
class Addition(binary_operation):
    def operate(self, x, y):
        return x + y

class Subtraction(binary_operation):
    def operate(self, x, y):
        return x - y

class Multiplication(binary_operation):
    def operate(self, x, y):
        return x * y

class Division(binary_operation):
    def operate(self, x, y):
        return x / y

class BinaryOperationFactory(object):
    def makeBinaryOperation(self, operator):
        if operator == '+':
            return Addition()
        if operator == '-':
            return Subtraction()
        if operator == '*':
            return Multiplication()
        if operator == '/':
            return Division()
    def getOperator(self, operator):
        return self.makeBinaryOperation(operator)

factory = BinaryOperationFactory()

add = factory.getOperator('+')
subtract = factory.getOperator('-')
multiply = factory.getOperator('*')
divide = factory.getOperator('/')

print("1 + 1 = ", add.operate(2,3))
print("2 - 3 = ", subtract.operate(2,3))
print("2 * 3 = ", multiply.operate(2,3))
print("2 / 3 = ", divide.operate(2,3))
