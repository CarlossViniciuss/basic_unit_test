import unittest

def add(a, b):
    return a + b

class TestCalculator(unittest.TestCase):

    def test_add_positive_numbers(self):
        # Arrange
        a = 4
        b = 3
        expected_result = 5
        
        # Act
        result = add(a, b)
        
        # Assert
        self.assertEqual(result, expected_result, "A adição de 2 e 3 deveria ser 5")

    def test_add_negative_numbers(self):
        # Arrange
        a = -1
        b = -1
        expected_result = -2
        
        # Act
        result = add(a, b)
        
        # Assert
        self.assertEqual(result, expected_result, "A adição de -1 e -1 deveria ser -2")

    def test_add_zero(self):
        # Arrange
        a = 0
        b = 0
        expected_result = 0
        
        # Act
        result = add(a, b)
        
        # Assert
        self.assertEqual(result, expected_result, "A adição de 0 e 0 deveria ser 0")

if __name__ == '__main__':
    unittest.main()
