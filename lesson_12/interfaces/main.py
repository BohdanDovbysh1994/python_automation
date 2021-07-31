from lesson_12.interfaces.helicopter import Helicopter

if __name__ == '__main__':
    helicopter = Helicopter()
    print(helicopter.engine_status)
    helicopter.start_engine()
    print(helicopter.engine_status)
    print(helicopter.get_coordinates())
    helicopter.move("up", 5)
    print(helicopter.get_coordinates())
    helicopter.move("forward", 10)
    print(helicopter.get_coordinates())
