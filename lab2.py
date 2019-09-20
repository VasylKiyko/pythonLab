dic = {'"': '&quot', '&': '&amp',
        '<': '&lt', '>': '&gt'}

def escape_str (string):
    esc_str = ''
    for x in string:
        if x in list(dic.keys()):
            esc_str += dic[x]
        else:
            esc_str += x
    return esc_str

def my_decorator(func):
    def wrapper(arg):
        func(arg)
        esc_str = escape_str(arg)
        print("Your escape HTML tag: {}".format(esc_str))
    return wrapper

@my_decorator
def show_string(string):
    print("This is your HTML teg: {}".format(string))

value = input("Write your HTML tag: ")
show_string(value)
