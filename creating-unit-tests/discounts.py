import unittest

def calculate_discount(price, discount_percentage):
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage cannot be negative nor greater than 100%")
    discounted_price = price * (1 - discount_percentage / 100)
    return discounted_price

class TestDiscountCalculation(unittest.TestCase):
    def test_valid_discount(self):
        result = calculate_discount(100, 20)
        self.assertEqual(result, 80)    # directly verifies if function return value (result) equals second parameter

    def test_invalid_discount_below_zero(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, -10)

    def test_invalid_discount_above_hundred(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, 150)

def main():
    TestDiscountCalculation()

if __name__ == '__main__':
    unittest.main()
