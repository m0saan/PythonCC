import unittest
from Employee import Employee

# Create a test using plenty of Employee instances.


# class employeeTestCase(unittest.TestCase):
#     """ Create a test for the Empoyee class. """

#     def test_give_default_raise(self):
#         my_employee = Employee("Mohammad", "Boustta")
#         self.assertEqual(my_employee.annual_salary, 0)

#     def test_give_custom_raise(self):
#         #annual_salary = 6000
#         my_employee = Employee("Mo", "Boustta")
#         my_employee.give_raise()
#         my_employee.give_raise(10000)
#         self.assertTrue(my_employee.annual_salary, 10000)


# unittest.main()

# Create a test using setUp() Hereby we'll use one Employee instance.


class employeeTestCase(unittest.TestCase):
    """ Create a test for the Empoyee class. """

    def setUp(self):
        self.my_employee = Employee("Mohammad", "Boustta")
        self.annual_salary = 10000

    def test_give_default_raise(self):
        self.assertEqual(self.my_employee.annual_salary, 0)

    def test_give_custom_raise(self):
        self.my_employee.give_raise()
        self.my_employee.give_raise(100000)
        self.assertTrue(self.my_employee.annual_salary, 100000)


unittest.main()
