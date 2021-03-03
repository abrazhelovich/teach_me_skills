import requests
import sys
from modules.img_types import img_form
from modules.check_size import rewrite, add, rewrite_full, add_full
from modules.is_folder_exist import check_folder


def headers_reading(url, mode):
    req = requests.get(url, stream=True)
    img_format = req.headers['Content-Type'].split('/')[1]
    img_size = req.headers['Content-Length']
    local_folder = 'images'
    check_folder(local_folder)
    file = url.split('/')[-1]
    path = f'{local_folder}/{file}'

    if req.status_code == 200:
        pass
        print(f'{req.status_code} OK')
    else:
        print(f'{req.status_code}')
        sys.exit()

    if img_format in img_form():
        pass
    else:
        print(f'{img_format} - Unknown picture format')
        sys.exit()

    if int(img_size) > 100000:
        if mode == 'rewrite' or mode is None:
            rewrite(req, path, file)

        if mode == 'add':
            add(req, path, local_folder, file)

        if mode == 'url_lst':
            print(f'File "{file}" hasn\'t been saved')
    else:

        if mode == 'rewrite' or mode is None:
            rewrite_full(req, path)

        if mode == 'add':
            add_full(req, path, local_folder, file)

        if mode == 'not_save':
            print(f'File "{file}" hasn\'t been saved')
    return req

