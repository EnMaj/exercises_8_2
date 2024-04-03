def decorator(func):
    def wrapper(*args, **kwargs):
        if func.__code__.co_argcount == 2:
            print(func(*args, **kwargs))
    return wrapper

@decorator
def test(a,b):
    return a,b

@decorator
def test_1(a,b,c):
    return a,b,c

test(1,2)
test_1(1,2,3)

