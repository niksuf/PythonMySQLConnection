import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('Successfully connected!')
    print('-' * 30)

    # DB query
    try:
        # create table
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT," \
        #                          " name varchar(32)," \
        #                          " password varchar(32)," \
        #                          " email varchar(32)," \
        #                          "PRIMARY KEY (id));"
        #     cursor.execute(create_table_query)
        #     print('Table created!')

        # insert data
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Nikita', 'qwertyui', " \
        #                    "'nikita@gmail.com');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #     print('Insert created!')

        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Alex', '12345', " \
        #                    "'alexa@gmail.com');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #     print('Insert created!')
        #
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Daria', 'qwertyui123', " \
        #                    "'daria@yandex.ru');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #     print('Insert created!')

        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Daria', 'Vvvvvvv', " \
        #                    "'daria2@yandex.ru');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #     print('Insert created!')
        #
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Daria', 'KillMe', " \
        #                    "'daria3@yandex.ru');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #     print('Insert created!')

        # update data
        # with connection.cursor() as cursor:
        #     update_query = "UPDATE `users` SET password = 'aaaAAAA' WHERE name = 'Daria'"
        #     cursor.execute(update_query)
        #     connection.commit()

        # delete data
        # with connection.cursor() as cursor:
        #     delete_query = "DELETE FROM `users` WHERE id = '2';"
        #     cursor.execute(delete_query)
        #     connection.commit()

        # drop table
        # with connection.cursor() as cursor:
        #     drop_table_query = "DROP TABLE `users`;"
        #     cursor.execute(drop_table_query)
        #     print('Table dropped!')
        #     print('-' * 30)

        # select all data from table
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `users`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print('-' * 30)

    # Close connection
    finally:
        connection.close()
except Exception as ex:
    print('Connection refused...')
    print(ex)
