import pytest

from calculator import calculator


class TestCalc:
def setup(self)
    self.calc = Calculator

    def test_multiply(self)
assert self.calc.multiply(self, 2, 4) == 8

 def test_adding(self)
assert self.calc.adding(self, 2, 3) == 5

 def test_division(self)
assert self.calc.division(self, 6, 3) == 2

 def test_zero_division(self)
with pytest.raises(self ZeroDivisionError) as e:
self.calc.division (1,0)
assert "division by zero" in str(e.value)

 def test_subtraction(self)
assert self.calc.subtraction(self, 2, 3) == -1 



