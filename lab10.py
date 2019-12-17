from urllib.request import urlopen, Request
from threading import Thread
# 'https://png2jpg.com/images/png2jpg/icon.png'


def thread_work(url, start, end):
    """задавати range скачування можна у header об'єкту Request"""
    _request = Request(url)
    _request.add_header('Range', f'bytes={str(start)}-{str(end)}')
    response = urlopen(_request)
    with open('file.png', 'ab') as _file:
        _file.seek(end, 0)  # 0 - з початку файлу
        _file.write(bytearray(response.read()))


def download(url, size):
    """кожен потік закачує 50 байт"""
    count = 0
    point = 0
    end = 100
    while True:
        if end > size:
            end = size

        thread = Thread(target=thread_work, args=(url, point, end))

        thread.start()
        count += 1
        thread.join()

        point = end
        end += 50
        if point == size:
            break

    print(f'{count} threads are working!')


if __name__ == '__main__':
    _url = 'https://png2jpg.com/images/png2jpg/icon.png' #input('Enter file url > ')
    file_info = dict(urlopen(_url).info())
    file_size = int(file_info['Content-Length'])
    download(_url, file_size)
