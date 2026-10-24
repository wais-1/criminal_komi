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
    except Exception as e:
        print(f'error: {e}')
        return False

def get_crime_card():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("select id, name, mini_description from crime order by name")
            crimes = cursor.fetchall()
        return crimes
    except Exception as e:
        print(f'error: {e}')

def get_suspect():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("select * from suspect")
            suspect = cursor.fetchone()
        return suspect
    except Exception as e:
        print(f'error: {e}')

def get_crime():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("select id, name, date, status, type, security_level, description from crime")
            crimes = cursor.fetchall()
        return crimes
    except Exception as e:
        print(f'error: {e}')

def get_clue():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("select name, date, type, description from clue")
            clues = cursor.fetchall()
        return clues
    except Exception as e:
        print(f'error: {e}')

def get_case():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("select case_number, article, opening_date, closing_date from criminal_case")
            cases = cursor.fetchall()
        return cases
    except Exception as e:
        print(f'error: {e}')

def get_crime_by_id(crime_id):
    try:
        conn = get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT id, name, description, date, status, type, security_level
                FROM crime
                WHERE id = %s
            """, (crime_id,))

            crime = cursor.fetchone()

        return crime

    except Exception as e:
        print(f"error: {e}")
        return None

def get_suspect_by_id(crime_id):
    try:
        conn = get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT suspect.id, suspect.full_name, suspect.birth_date, suspect.distinguishing_marks, suspect.status
                FROM suspect
                JOIN suspect_crime ON suspect.id=suspect_crime.id_suspect
                WHERE suspect_crime.id_crime = %s
            """, (crime_id,))

            crime = cursor.fetchone()

        return crime

    except Exception as e:
        print(f"error: {e}")
        return None

def get_clue_by_id(crime_id):
    try:
        conn = get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT clue.id, clue.name, clue.date, clue.type, clue.description
                FROM clue
                JOIN crime ON crime.id=clue.id_crime
                WHERE crime.id = %s
            """, (crime_id,))

            crime = cursor.fetchone()

        return crime

    except Exception as e:
        print(f"error: {e}")
        return None

def get_case_by_id(crime_id):
    try:
        conn = get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT criminal_case.id, criminal_case.case_number, criminal_case.opening_date, criminal_case.closing_date, criminal_case.article
                FROM criminal_case
                JOIN crime ON crime.id=criminal_case.id_crime
                WHERE crime.id = %s
            """, (crime_id,))

            crime = cursor.fetchone()

        return crime

    except Exception as e:
        print(f"error: {e}")
        return None