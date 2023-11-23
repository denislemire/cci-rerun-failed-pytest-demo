import pytest
from src.mymath import MyMath

class TestMyMath:
	def test_add(self):
		assert MyMath.add(2, 3) == 5

	def test_subtract(self):
		assert MyMath.subtract(5, 3) == 2

	def test_multiply(self):
		assert MyMath.multiply(3, 4) == 12

	def test_divide(self):
		assert MyMath.divide(8, 4) == 2
		with pytest.raises(ValueError):
			MyMath.divide(10, 0)
