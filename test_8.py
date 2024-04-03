import datetime

def log_file(func):
        def wrapper(*args, **kwargs):
            with open('log_file.txt', 'w') as log:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    log.write(f'{datetime.datetime.now()} {type(err)} {err}\n')
        return wrapper

@log_file
def a(c,d):
    return c/d

a(1,0)
