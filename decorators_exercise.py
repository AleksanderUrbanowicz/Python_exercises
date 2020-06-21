from functools import wraps


def outer_function(msg):
    message = 'msg defined in outer_function'

    def inner_function():
        print(message)
        print(msg)

    return inner_function


my_function1 = outer_function('msg argument1')
my_function2 = outer_function('msg argument2')


# my_function1()
# my_function2()


# Decorator is a function that takes another function as an argument
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper execution')
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display():
    print('display func')


@decorator_function
def display_with_arguments(msg):
    print('display_with_arguments: ' + msg)


# decorated_display = decorator_function(display)
# decorated_display()


# display()
# display_with_arguments('display argument')


# Classes as decorators
class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('__call__ method execution')
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display_cls():
    print('display_cls func')


@DecoratorClass
def display_cls_with_arguments(msg):
    print('display_cls_with_arguments: ' + msg)


# display_cls()
# display_cls_with_arguments('display_cls argument')


def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logging.info('args: {}, kwargs: {}'.format(args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function):
    import time

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = original_function(*args, **kwargs)
        time_delta = time.time() - start_time
        print('{} Run time: {} sec'.format(original_function.__name__, time_delta))
        return result

    return wrapper


@my_logger
def display_logger_with_arguments(msg):
    print('display_logger_with_arguments: ' + msg)


@my_logger
@my_timer
def display_timer_with_arguments(msg):
    print('display_timer_with_arguments: ' + msg)


display_logger_with_arguments('display with logger argument')
display_timer_with_arguments('with timer argument')
