def img_form():
    with open('modules/available_img_formats.txt', 'r') as file:
        return file.read()
