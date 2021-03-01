import os


def check_folder(local_folder):
    if os.path.exists(local_folder):
        pass
    else:
        os.mkdir(local_folder)

