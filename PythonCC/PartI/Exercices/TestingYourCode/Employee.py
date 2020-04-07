class Employee():

    def __init__(self, first_name, last_name, annual_salary=0):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, add_to_salary=0):
        if not self.annual_salary:
            self.annual_salary = 5000
        else:
            self.annual_salary = add_to_salary


if __name__ == "__main__":
    my_employee = Employee("MO", "Boustta")
    my_employee.give_raise()
    my_employee.give_raise(10000)
    print(my_employee.annual_salary)
