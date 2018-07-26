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

factory = BinaryOperationFactory();

add = factory.getOperator('+');
subtract = factory.getOperator('-');
multiply = factory.getOperator('*');
divide = factory.getOperator('/');

print("1 + 1 = ", add.operate(1,1))
print("5 - 3 = ", subtract.operate(5,3))
print("3 * 4 = ", multiply.operate(3,4))
print("17 / 2 = ", divide.operate(17,2))
