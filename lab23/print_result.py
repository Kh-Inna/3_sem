def print_result(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f"{func.__name__}")
        if isinstance(res, list):
            for r in res:
                print (r)
        elif isinstance(res, dict):
            for x, y in res.items():
                print (x, " = ", y)
        else:
            print(res)
        return res
    return wrapper

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()