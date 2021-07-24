def sum(a, b):
    try:
        assert 1 == 0
        return [a, b]
    except Exception as e:
        return []
    except AssertionError as e:
        return []
    finally:
        print("Alwais will be printed")


print(sum(1, "str"))
