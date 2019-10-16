dic = {'"': '&quot', '&': '&amp', '<': '&lt', '>': '&gt'}


def escape_str(string):
    str_list = [x for x in string]
    for x in range(len(str_list)):
        if str_list[x] in list(dic.keys()):
            str_list[x] = dic.get(str_list[x])
    return ''.join(str_list)


def my_decorator(func):
    def wrapper(*args, **kwargs):
        tag = func(*args, **kwargs)
        esc_str = escape_str(tag)
        return esc_str
    return wrapper


@my_decorator
def show_string(string):
    return string


if __name__ == '__main__':
    value = input("Write your HTML tag: ")
    print('Your escape HTML tag: {}'.format(show_string(value)))
