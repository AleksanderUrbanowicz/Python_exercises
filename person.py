import datetime as dt


class Person:
    number_of_ppl = 0

    def __init__(self, first, last, birth_date):
        self.first = first
        self.last = last
        self.birth_date = birth_date
        self.id = Person.number_of_ppl
        Person.number_of_ppl += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def age(self):
        today = dt.date.today()
        years = today.year - self.birth_date.year

        if (today.month < self.birth_date.month or
                (today.month == self.birth_date.month and
                 today.day < self.birth_date.day)):
            years = years - 1
        return years

    @staticmethod
    def get_number_of_ppl():
        return Person.number_of_ppl

    def __str__(self):
        print(f'{self.id}.{self.first} {self.last}, age: {self.age()}')

    @classmethod
    def from_string(cls, person_str):
        first, last, date = person_str.split(' ')
        birth_date = date.split('-')
        return cls(first, last, dt.date(int(birth_date[0]), int(birth_date[1]), int(birth_date[2])))


class Employee(Person):
    company_email = 'email.com'

    def __init__(self, first, last, birth_date, pay, phone_number):
        super().__init__(first, last, birth_date)
        self.pay = pay
        self.phone_number = phone_number
        self.email = first + '.' + last + '@' + Employee.company_email


class Manager(Employee):
    def __init__(self, first, last, birth_date, pay, phone_number, employees=None):
        super().__init__(first, last, birth_date, pay, phone_number)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def list_employees(self):
        print(f'Employees of {self.fullname()} are:')
        for emp in self.employees:
            print(f'{emp.fullname()}')


person_string = 'John Doe 1985-3-13'
person1 = Person.from_string(person_string)
employee1 = Employee('John', 'Doe', dt.date(1980, 6, 22), 7000, 1234321)
employee2 = Employee('Jane', 'Doe', dt.date(1990, 8, 2), 7000, 9876543)
manager1 = Manager('Michael', 'Scott', dt.date(1970, 6, 12), 10000, 4574575, [employee1, employee2])

person1.__str__()
employee1.__str__()
employee2.__str__()
manager1.__str__()

print(f'Number of ppl: {Person.number_of_ppl}')
manager1.list_employees()

print(issubclass(Employee, Person))
print(issubclass(Person, Employee))
print(isinstance(employee1, Person))
