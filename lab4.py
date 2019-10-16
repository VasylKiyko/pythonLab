def wraps(str_func):        # тут декоратор приймає як аргумент функцію get_string, яка не є функцією яка декорується
    def wrapper(wrapper_func):      # а wrapper_func вже декорована функція wrapper з декоратора decorator
        wrapper_func.__name__ = str_func.__name__
        wrapper_func.__doc__ = str_func.__doc__
        return wrapper_func
    return wrapper


def decorator(func):
    @wraps(func)        # в якості аргумента wraps функція get_string
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return value
    return wrapper


@decorator
def get_string(string):
    """here are some txt"""
    return string


if __name__ == '__main__':
    print('Call function')
    print(get_string.__name__)
    print(get_string.__doc__)
    