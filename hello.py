class Calculator:
    def add(self, num1, num2):
        return num1+num2

    def subtract(self, num1, num2):
        return num1-num2

    def multiply(self, num1, num2):
        return num1*num2

    def divide(self, num1, num2):
        if num2 == 0:
            return 0
        else:
            return num1/num2

    def main(self):
        print(self.add(3, 4))
        print(self.subtract(3, 4))
        print(self.multiply(3, 4))
        print(self.divide(3, 4))

calc = Calculator()
calc.main()
