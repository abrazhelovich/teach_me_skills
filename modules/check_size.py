import os
from modules.random_string import generate_random_string

rand_str = generate_random_string()
text = f'File downloaded successfully'


def common(req, file, picture):
    for chunk in req.iter_content(chunk_size=40000):
        picture.write(chunk)
    print(text)


def rewrite(req, path, file):
    with open(path, 'wb') as picture:
        common(req, file, picture)


def add(req, path, folder, file):
    if not os.path.exists(path):
        with open(path, 'wb') as picture:
            common(req, file, picture)
    else:
        r_str = f'({rand_str})_{file}'
        with open(f'{folder}/{r_str}', 'wb') as picture:
            common(req, file, picture)


def rewrite_full(req, path):
    with open(path, 'wb') as picture:
        picture.write(req.content)
        print(text)


def add_full(req, path, folder, file):
    if not os.path.exists(path):
        with open(path, 'wb') as picture:
            picture.write(req.content)
            print(text)
    else:
        r_str = f'({rand_str})_{file}'
        with open(f'{folder}/{r_str}', 'wb') as picture:
            picture.write(req.content)
            print(text)


