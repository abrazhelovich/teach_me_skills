import requests
import sys
from modules.check_size import rewrite, add, rewrite_full, add_full


def get_image(url, mode, avail_img_format, folder):
    file = url.split('/')[-1]
    path = f'{folder}/{file}'
    req = requests.get(url, stream=True)
    img_format = req.headers['Content-Type'].split('/')[1]
    img_size = req.headers['Content-Length']

    if req.status_code == 200:
        print(f'{req.status_code} OK')
    else:
        print(f'{req.status_code}')
        sys.exit()

    if img_format in avail_img_format:
        pass
    else:
        print(f'{img_format} - Unknown picture format')
        sys.exit()

    if int(img_size) > 100000:
        if mode == 'rewrite' or mode is None:
            rewrite(req, path, file)

        if mode == 'add':
            add(req, path, folder, file)

        if mode == 'not_save':
            print(f'File "{file}" hasn\'t been saved')
    else:

        if mode == 'rewrite' or mode is None:
            rewrite_full(req, path)

        if mode == 'add':
            add_full(req, path, folder, file)

        if mode == 'not_save':
            print(f'File "{file}" hasn\'t been saved')
    return req


