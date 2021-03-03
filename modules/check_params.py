from modules.my_exceptions import ParamsIncorrect
from modules.headers_reading import headers_reading
from modules.urls_reading import urls_reading


def check_params(url, urls, mode):
    if (url is None and urls is None) or (url is not None and urls is not None):
        raise ParamsIncorrect
    elif url is not None and urls is None:
        headers_reading(url, mode)
    elif url is None and urls is not None:
        urls_reading(urls, mode)

