import pymysql

def get_db_connection():
    return pymysql.connect(
        host = 'localhost',
        port = 8889,
        user = 'root',
        password = 'root',
        database = 'criminal_komi'
    )

def set_user(login, password):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("insert into user(login, password, id_role) values (%s, %s, 5)", (login, password))
            conn.commit()
            return True
            # conn.close()
    except Exception as e:
        print(f'error: {e}')
        return False