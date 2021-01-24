# Дан текстовый файл, содержащий различные даты.
# Каждая дата - это число, месяц и год. Найти самую
# раннюю дату.

from datetime import datetime

def main(file: str) -> str:
    """This function founs out the earlierst date from file

    The file contains list of dates wich needed to handle and define the earliest date

    Parameters
    ----------
    file : str
        File name with list of dates following format: %Y-%m-%d

    Returns
    -------
    str
        The earliest date
    """

    with open(file) as file:
        newst = datetime.strptime(file.readline().strip('\n'), '%Y-%m-%d')
        for date in file:
            current_date = datetime.strptime(date.strip('\n'), '%Y-%m-%d')
            if newst > current_date:
                newst = current_date
    return datetime.strftime(newst, '%d-%m-%Y')

if __name__ == '__main__':
    file_name = 'task_01.txt'
    file_txt = main(file_name)
    print(f'This is the earliest date from the list: {file_txt}')
