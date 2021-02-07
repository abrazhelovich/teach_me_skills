from db_module import create_db, add_records, get_data, del_data, update_data


def user_menu(db_name, prods, table, comment, product_id):
    val = int(input('''1.Create DB
2.Add new record
3.Get data
4.Delete by product id
5.Update by product id

Make a choice: '''))

    if val == 1:
        create_db(db_name)
        print('SQLite DB created')

    if val == 2:
        add_records(db_name, prods, table)
        print(get_data(db_name, table))

    if val == 3:
        print(get_data(db_name, table))

    if val == 4:
        del_data(db_name, table, product_id)
        print(get_data(db_name, table))

    if val == 5:
        update_data(db_name, table, product_id, comment)
        print(get_data(db_name, table))
