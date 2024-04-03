import functools
#Функциональное программирование
#Понятие функции

from datetime import datetime

def get_second():
    '''Return current seconds'''
    return datetime.now().second

def split_tags(tag_string):
    tag_list = []
    for tag in tag_string.split(','):
        tag_list.append(tag.strip())
    return tag_list

def add(x: int, y: int) -> int:
    return x + y

def externder(sourse_list, extend_list):
    sourse_list.extend(extend_list)

def replacer(sourse_tuple, replace_with):
    sourse_tuple = replace_with

user_info = ("invanov ivan", "02/12")
replacer(user_info,("petrov petr", "05/13"))
print()

def say(greeting, name):
    print(f'{greeting}, {name}')

say(name= "Kitty", greeting= "Hello")

def greeting(name= 'it\'s me...'):
    print(f'Hi, {name}!')

def append_one(iterable=[]):
    iterable.append(1)
    return iterable

def function(iterable=None):
    if iterable is None:
        iterable = []
    iterable.append(1)
    return iterable

def function_2(iterable=None):
    iterable = iterable or []
    iterable.append(1)
    return iterable

def printer(*args):
    print(type(args))
    for arg in args:
        print(arg)

name_list = ['andray', 'anna', 'alex']
printer(*'USA')

def printer_2(**kwargs):
    print(type(kwargs))
    for key,val in kwargs.items():
        print(f'{key}: {val}')

student = {
    'name' : 'Ivanov Ivan',
    'feedback' : {'courses': ['programming','mor'],
                  'marks' : [5, 5]
                  }
}

printer_2(**student)

def caller(func, params):
    return func(*params)

def printer(name, origin):
    print(f'I\'m {name} of {origin}.')

caller(printer,['Alex', 'Montenegro'])

def get_multiplier():
    def inner(a, b):
        return a * b
    return inner

multiplier = get_multiplier()
print(multiplier(10,11))

def get_multiplier(number):
    def inner(a):
        return a * number
    return inner

multiplier_by_2 = get_multiplier(2)
multiplier_by_10 = get_multiplier(10)
print(multiplier_by_2(20),multiplier_by_10(20))

def squarify(a):
    return a**2

print(list(map(squarify(), range(5))))


def greeter(person, greeting):
    return f'{person}, {greeting}'

hier = functools.partial(greeter, greeting="Hi")
helloer = functools.partial(greeter, greeting="Hello")

print(hier('brother'))
print(helloer("sir"))

print(x**2 for x in range(10))


#декораторы
def decorator(func):
    print("А я тут... ахахахх")
    return func

@decorator
def decorated():
    print("Hello!")

decorated()