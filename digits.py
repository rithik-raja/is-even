class Digits:
    '''
    A static class used to access the properties of digits.
    '''
    digits = isDigitEven = None
    def load():
        Digits.digits = list(range(10))
        Digits.isDigitEven = [not digit % 2 for digit in Digits.digits]