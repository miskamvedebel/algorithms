class RegressionLine():
    def __init__(self, X, Y):
        
        self.x = self._validate(A=X, datatype=list)
        self.y = self._validate(A=Y, datatype=list)
        self.N = self._validate_length()

        self.sum_x = sum(self.x)
        self.sum_y = sum(self.y)
        self.sum_x_square = sum([xx ** 2 for xx in self.x])
        self.sum_xy = sum([xx * yy for xx, yy in zip(self.x, self.y)])
        self.denominator = self.N * self.sum_x_square - self.sum_x ** 2

        self.a = (self.sum_x_square * self.sum_y - self.sum_x * self.sum_xy) / self.denominator
        self.b = (self.N * self.sum_xy - self.sum_x * self.sum_y) / self.denominator

    # @property
    # def x(self) -> list:
    #     return self._x
    
    # @x.setter
    # def x(self, value: str) -> None:
    #     if not isinstance(value, list):
    #         raise TypeError("X must be a list")
    #     self._name = value

    def _validate(self, A: list, datatype: object = list):
        if not isinstance(A, list):
            raise TypeError(f"{A=} has incorrect datatype, should be {datatype.__name__}")
        return A
    
    def _validate_length(self):
        if len(self.x) != len(self.y):
            raise TypeError("Length of X and Y are not matching")
        return len(self.x)

    def find_slope(self, n_decimal=4):
        return (round(self.a, n_decimal), round(self.b, n_decimal))
        

rl = RegressionLine(X=[5, 10, 34, 56, 56, 67], Y=[78, 70, 65, 58, 48, 13])
print(rl.find_slope())