import unittest
from employee import employee


class EmployeeTest(unittest.TestCase):
    def full_employee(self):
        """Does this work?"""
        james = employee('James', 'Dixon', 12000)
        self.assertEqual(james, 'James Dixon - Salary 12000')


if __name__ == '__main__':
    unittest.main()

