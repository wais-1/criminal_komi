import pymysql

def get_db_connection():
    return pymysql.connect(
        host = 'localhost',
        port = 8889,
        user = 'root',
        password = 'root',
        database = 'criminal_komi'
    )

def set_user():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("insert into user(login, password, id_role) values ('test_user', 'user', 5)")
        conn.commit()
        conn.close()