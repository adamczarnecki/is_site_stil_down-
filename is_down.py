import urllib.request
import datetime
import sys


def is_url_work(url):
    try:
        resp = urllib.request.urlopen(url, timeout=5)
    except Exception as e:
        return False, e
    else:
        return True, resp.getcode()


def prepare_url(url):
    if 'http://' in url or 'https://' in url:
        pass
    else:
        url = 'http://' + url
    return url


def print_if_its_work(url):
    czas = datetime.datetime.now()
    print(f'{czas}\tStrona: {url.upper()}\t', end="")
    is_work, code = is_url_work(prepare_url(url))
    if is_work:
        print('DZIAŁA!!!!!', code)
    else:
        print('Dalej leży ;(', code)
    return is_work


if __name__ == '__main__':
    try:
        url = sys.argv[1]
    except IndexError:
        print('Podaj adres strony do sprawdzenia')
    try:
        ok = 0
        while ok < 30:
            ok += print_if_its_work(url)
        print('Zamykam')
    except KeyboardInterrupt:
        print('Zamykam')
