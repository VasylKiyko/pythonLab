def add_tag_function(tag=""):
    def html_decoratot(func):
        def wrapper(*args, **kwargs):
            s = func(*args, **kwargs)
            return "<{0}>{1}</{0}>".format(tag, s)  # return <tag>string</tag>
        return wrapper
    return html_decoratot


@add_tag_function("html")
def get_string(string):
    return string


if __name__ == '__main__':
    value = input("Write your HTML text: ")
    print(get_string(value))
