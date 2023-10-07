class IsEvenChecker:
    '''
    A class that, when loaded with a number, applies the necessary operations to check whether it is even.
    '''
    Digits = None # static attribute set when constructor first called

    def __init__(self):
        if IsEvenChecker.Digits is None:
            try:
                # lazy loading the digits package to reduce latency
                from digits import Digits
                IsEvenChecker.Digits = Digits
                Digits.load()
            except ImportError:
                raise ImportError(
                    "Failed to import the `digits` package. "
                    "Are you sure it's installed and available on your PYTHONPATH environment variable? "
                    "Did you forget to activate a virtual environment?"
                )   
        self.hasBeenChecked = False
        self.loadedValue = None
        self.result = None

    def loadValue(self, val):
        if not isinstance(val, int):
            raise ValueError(f"Illegal argument: Expected int but got {type(val).__name__}")
        self.hasBeenChecked = False
        self.loadedValue = val
        self.result = None

    def runCheck(self):
        '''
        Core algorithm to check if given number is even.
        '''
        if self.loadedValue is None:
            raise RuntimeError("Fatal exception: The IsEvenChecker instance has not been loaded with a value.")
        valList = [digit for digit in str(self.loadedValue)] # obtain digits
        valList = list(map(int, valList)) # cast the digits to ints
        valIndices = [IsEvenChecker.Digits.digits.index(digit) for digit in valList] # get the corresponding indices in the digits class
        areDigitsEven = [IsEvenChecker.Digits.isDigitEven[valIndex] for valIndex in valIndices] # match the indices to the boolean of whether they are even
        ptr = 0 # initialize pointer
        while ptr < len(areDigitsEven) - 1: # shift the pointer until we reach the last digit
            ptr = ptr + 1
        self.hasBeenChecked = True # set flag to indicate processing is complete
        self.result = areDigitsEven[ptr] # access the last element to determine whether number is even
    
    def exportResult(self):
        if not self.hasBeenChecked:
            raise RuntimeError("Fatal exception: The IsEvenChecker instance has not run the check yet.")
        return self.result
    
if __name__ == "__main__":
    isEvenChecker = IsEvenChecker()
    isEvenChecker.loadValue(2502)
    isEvenChecker.runCheck()
    isEven = isEvenChecker.exportResult()
    print("Even" if isEven else "Odd") # Even