import time


def time_limit(func):
    def wrapped(*args, **kwargs):
        wrapped.count += 1
        start = time.time()
        print(start)
        func(*args, **kwargs)
        if time.time() - start > 3:
            raise Exception('Timeout Exception!!')
        elif wrapped.count > 2:
            raise Exception('Count Exeption')
    wrapped.count = 0
    return wrapped




@time_limit
def test_run():
    print(777)

test_run()
test_run()
test_run()