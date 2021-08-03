from lesson_13.buiding_example.building import Building
from lesson_13.buiding_example.company import Company

if __name__ == '__main__':
    building = Building("Nova", "Backer street 32")
    print(len(building))
    toyota = Company("Toyota", "Auto Industry")
    lexus = Company("Lexus", "Auto Industry")
    building[0] = toyota
    building[1] = lexus
    print(len(building))
    print(building[0])
