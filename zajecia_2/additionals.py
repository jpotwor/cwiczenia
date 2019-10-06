import numpy as np


def function_2(x, y):
    return int(x * y)


# wywolanie funkcji argumenty sa tuple, a key word argumenty sa dictem
def function(first_argument, *args, **kwargs):
    print('First required argument: {}'.format(first_argument))
    print('Args: {}'.format(args))
    print('Kwargs: {}'.format(kwargs))
    print('Printing value of print_this argument: {}'.format(kwargs.get('print_this')))
    step = function_2(args[1], 1)
    new_step = kwargs.get('new_step')
    if new_step:
        step = new_step
    return np.arange(first_argument, args[0], step)


print(function(10, 101, 3, 'unused', keywordarg='anything', print_this='Hello', new_step=10))

arguments = [21, 10, 10, 10, 10]
kwarguments = {'new_step': 1, 'next': 'WOW'}

print(function(*arguments, **kwarguments))
