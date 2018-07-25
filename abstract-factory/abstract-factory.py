import abc


class binary_operation(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def operate(self, x, y):
      """Run a binary operation and return the result"""
      return



class Addition(binary_operation):
    def operate(x, y):
        return x + y

class Subtraction(binary_operation):
    def operate(x, y):
        return x - y

class Multiplication(binary_operation):
    def operate(x, y):
        return x * y

class Division(binary_operation):
    def operate(x, y):
        return x / y

