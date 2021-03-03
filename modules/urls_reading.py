from modules.headers_reading import headers_reading


def urls_reading(urls, mode):
    with open(urls) as file:
        for row in file:
            headers_reading(row.strip(), mode)

