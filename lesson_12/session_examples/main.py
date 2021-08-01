from datetime import datetime

from lesson_12.session_examples.company import Company
from lesson_12.session_examples.employee import Employee

if __name__ == '__main__':
    toyota = Company(
        "Toyota",
        "Backer street 32 London",
        datetime.now(),
        "Auto Industry"
    )

    john = Employee("John", 32, "Engineering", 1500, "Network Engineer")
    marta = Employee("Marta", 50, "Engineering", 100, "Software engineer")
    james = Employee("James", 99, "Managemenet", 2000, "Project manager")
    anton = Employee("Anton", 23, "HR", 500, "Hr manager")
    alex = Employee("Alex", 14, "PR", 2500, "Pr manager")

    print(toyota.employees)
    toyota.hire(john)
    toyota.hire(marta)
    toyota.hire(james)
    print(toyota.employees)
