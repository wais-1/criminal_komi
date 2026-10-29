import pymysql
import re
def get_db_connection():
    return pymysql.connect(
        host = 'localhost',
        port = 8889,
        user = 'root',
        password = 'root',
        database = 'criminal_komi'
    )

#регистрация пользователя
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

#получение карточки преступления для отображения
def get_crime_card():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("select id, name, mini_description from crime order by name")
            crimes = cursor.fetchall()
        return crimes
    except Exception as e:
        print(f'error: {e}')

def get_username(user_id):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("select login from user where id = $s", (user_id,))
            user = cursor.fetchone()
        return user[0]
    except Exception as e:
        print(f'error: {e}')
    finally:
        if conn:
            conn.close()

#получение данных по id для корректного открытия окна преступления через карточку
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
    finally:
        if conn:
            conn.close()

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
    finally:
        if conn:
            conn.close()

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
    finally:
        if conn:
            conn.close()

def get_case_by_id(crime_id):
    try:
        conn = get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT criminal_case.id, criminal_case.case_number, criminal_case.opening_date, criminal_case.closing_date, criminal_case.article, criminal_case.id_interrogation_record
                FROM criminal_case
                JOIN crime ON crime.id=criminal_case.id_crime
                WHERE crime.id = %s
            """, (crime_id,))

            crime = cursor.fetchone()

        return crime

    except Exception as e:
        print(f"error: {e}")
        return None
    finally:
        if conn:
            conn.close()

def get_record_by_crime_id(crime_id):
    conn = get_db_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT
                    interrogation_record.id,
                    interrogation_record.text,
                    interrogation_record.audio_url,
                    interrogation_record.video_url,
                    interrogation_record.date,
                    witness.full_name,
                    witness.witness_reliability_levels,
                    witness.program_stages,
                    victim.full_name,
                    victim.birth_date,
                    victim.severity,
                    victim.protection_statuses
                FROM criminal_case
                JOIN crime
                    ON crime.id = criminal_case.id_crime
                JOIN interrogation_record
                    ON interrogation_record.id = criminal_case.id_interrogation_record
                LEFT JOIN witness
                    ON witness.id = interrogation_record.id_witness
                LEFT JOIN victim
                    ON victim.id = interrogation_record.id_victim
                WHERE crime.id = %s
            """, (crime_id,))

            record = cursor.fetchone()

        return record

    except Exception as e:
        print(f"error: {e}")
        return None

    finally:
        if conn:
            conn.close()

#получение enum для отображения в окнах добавления и редактирования
def get_crime_status():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SHOW COLUMNS FROM crime LIKE 'status'")
            status = cursor.fetchone()

            if not status:
                return []
            enum_status = status[1]
            statuses = re.findall(r"'((?:[^'\\]|\\.)*)'", enum_status)
            return [(i, status) for i, status in enumerate(statuses)]
        conn.close()
        return status
    except Exception as e:
        print(f'error: {e}')

def get_crime_type():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SHOW COLUMNS FROM crime LIKE 'type'")
            crime_type = cursor.fetchone()

            if not crime_type:
                return []
            enum_type = crime_type[1]
            types = re.findall(r"'((?:[^'\\]|\\.)*)'", enum_type)
            return [(i, crime_type) for i, crime_type in enumerate(types)]
        conn.close()
        return status
    except Exception as e:
        print(f'error: {e}')

def get_crime_security():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SHOW COLUMNS FROM crime LIKE 'security_level'")
            security = cursor.fetchone()

            if not security:
                return []
            enum_security = security[1]
            security_levels = re.findall(r"'((?:[^'\\]|\\.)*)'", enum_security)
            return [(i, security) for i, security in enumerate(security_levels)]
        conn.close()
        return status
    except Exception as e:
        print(f'error: {e}')

def get_suspect_status():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SHOW COLUMNS FROM suspect LIKE 'status'")
            security = cursor.fetchone()

            if not security:
                return []
            enum_security = security[1]
            security_levels = re.findall(r"'((?:[^'\\]|\\.)*)'", enum_security)
            return [(i, security) for i, security in enumerate(security_levels)]
        conn.close()
        return status
    except Exception as e:
        print(f'error: {e}')

def get_clue_type():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SHOW COLUMNS FROM clue LIKE 'type'")
            security = cursor.fetchone()

            if not security:
                return []
            enum_security = security[1]
            security_levels = re.findall(r"'((?:[^'\\]|\\.)*)'", enum_security)
            return [(i, security) for i, security in enumerate(security_levels)]
        conn.close()
        return status
    except Exception as e:
        print(f'error: {e}')

def get_location_type():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SHOW COLUMNS FROM crime_location LIKE 'object_type'")
            security = cursor.fetchone()

            if not security:
                return []
            enum_security = security[1]
            security_levels = re.findall(r"'((?:[^'\\]|\\.)*)'", enum_security)
            return [(i, security) for i, security in enumerate(security_levels)]
        conn.close()
        return status
    except Exception as e:
        print(f'error: {e}')

def get_victim_status():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SHOW COLUMNS FROM victim LIKE 'protection_statuses'")
            security = cursor.fetchone()

            if not security:
                return []
            enum_security = security[1]
            security_levels = re.findall(r"'((?:[^'\\]|\\.)*)'", enum_security)
            return [(i, security) for i, security in enumerate(security_levels)]
        conn.close()
        return status
    except Exception as e:
        print(f'error: {e}')

def get_witness_levels():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SHOW COLUMNS FROM witness LIKE 'witness_reliability_levels'")
            security = cursor.fetchone()

            if not security:
                return []
            enum_security = security[1]
            security_levels = re.findall(r"'((?:[^'\\]|\\.)*)'", enum_security)
            return [(i, security) for i, security in enumerate(security_levels)]
        conn.close()
        return status
    except Exception as e:
        print(f'error: {e}')

def get_witness_stages():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SHOW COLUMNS FROM witness LIKE 'program_stages'")
            security = cursor.fetchone()

            if not security:
                return []
            enum_security = security[1]
            security_levels = re.findall(r"'((?:[^'\\]|\\.)*)'", enum_security)
            return [(i, security) for i, security in enumerate(security_levels)]
        conn.close()
        return status
    except Exception as e:
        print(f'error: {e}')

def get_suspects():
    try:
        conn = get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT id, full_name
                FROM suspect
                ORDER BY full_name
            """)

            return cursor.fetchall()

    except Exception as e:
        print(f"error: {e}")
        return None

def get_crimes():
    try:
        conn = get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT id, name
                FROM crime
                ORDER BY name
            """)

            return cursor.fetchall()

    except Exception as e:
        print(f"error: {e}")
        return None

#добавление и обновление данных УД
def set_criminal_case(case_number, opening_date, closing_date, article, id_interrogation_record, id_investigator, id_crime):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("insert into criminal_case(case_number, opening_date, closing_date, article, id_interrogation_record, id_investigator, id_crime) values (%s, %s, %s, %s, %s, %s, %s)", 
                           (case_number, opening_date, closing_date, article, id_interrogation_record, id_investigator, id_crime))
            conn.commit()
            conn.close()
            return True
    except Exception as e:
        print(f'error: {e}')
        return False

def update_criminal_case(case_id, case_number, opening_date, closing_date, article, id_interrogation_record, id_investigator, id_crime):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("update criminal_case set case_number = %s, opening_date = %s, closing_date = %s, article = %s, id_interrogation_record = %s, id_investigator = %s, id_crime = %s where id = %s",
                           (case_number, opening_date, closing_date, article, id_interrogation_record, id_investigator, id_crime, case_id))
        if cursor.rowcount == 0:
            cursor.execute(
                "SELECT id FROM criminal_case WHERE id = %s",
                (case_id,)
            )

            if cursor.fetchone() is None:
                print(f"Дело с ID {case_id} не найдено")
                return False
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'error: {e}')
        return False

#добавление и обновление данных преступления
def set_crime(name, mini_description, description, date, status, crime_type, security_level, id_crime_location):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("insert into crime(name, mini_description, description, date, status, type, security_level, id_crime_location) values (%s, %s, %s, %s, %s, %s, %s, %s)", 
                           (name, mini_description, description, date, status, crime_type, security_level, id_crime_location))
            conn.commit()
            conn.close()
            return True
    except Exception as e:
        print(f'error: {e}')
        return False

def update_crime(crime_id, name, mini_description, description, date, status, crime_type, security_level, id_crime_location):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("update crime set name = %s, mini_description = %s, description = %s, date = %s, status = %s, type = %s, security_level = %s, id_crime_location = %s where id = %s",
                           (name, mini_description, description, date, status, crime_type, security_level, id_crime_location, crime_id))
        if cursor.rowcount == 0:
            cursor.execute(
                "SELECT id FROM crime WHERE id = %s",
                (crime_id,)
            )

            if cursor.fetchone() is None:
                print(f"Дело с ID {crime_id} не найдено")
                return False
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'error: {e}')
        return False

#добавление и обновление данных улики
def set_clue(name, date, clue_type, description, id_crime):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("insert into clue(name, date, type, description, id_crime) values (%s, %s, %s, %s, %s)", 
                           (name, date, clue_type, description, id_crime))
            conn.commit()
            conn.close()
            return True
    except Exception as e:
        print(f'error: {e}')
        return False

def update_clue(clue_id, name, date, clue_type, description, id_crime):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("update clue set name = %s, date = %s, type = %s, description = %s, id_crime = %s, where id = %s",
                           (name, date, clue_type, description, id_crime, clue_id))
        if cursor.rowcount == 0:
            cursor.execute(
                "SELECT id FROM clue WHERE id = %s",
                (clue_id,)
            )

            if cursor.fetchone() is None:
                print(f"Дело с ID {clue_id} не найдено")
                return False
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'error: {e}')
        return False

#добавление и обновление данных подозреваемого
def set_suspect(full_name, img_url, birth_date, distinguishing_marks, status):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("insert into suspect(full_name, img_url, birth_date, distinguishing_marks, status) values (%s, %s, %s, %s, %s)", 
                           (full_name, img_url, birth_date, distinguishing_marks, status))
            conn.commit()
            conn.close()
            return True
    except Exception as e:
        print(f'error: {e}')
        return False

def update_suspect(suspect_id, full_name, img_url, birth_date, distinguishing_marks, status):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("update suspect set full_name = %s, img_url = %s, birth_date = %s, distinguishing_marks = %s, status = %s where id = %s",
                           (full_name, img_url, birth_date, distinguishing_marks, status, suspect_id))
        if cursor.rowcount == 0:
            cursor.execute(
                "SELECT id FROM suspect WHERE id = %s",
                (suspect_id,)
            )

            if cursor.fetchone() is None:
                print(f"Дело с ID {suspect_id} не найдено")
                return False
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'error: {e}')
        return False

#добавление связей между преступником и преступлением
def set_suspect_crime(id_suspect, id_crime):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("insert into suspect_crime(id_suspect, id_crime) values (%s, %s)", 
                           (id_suspect, id_crime))
            conn.commit()
            conn.close()
            return True
    except Exception as e:
        print(f'error: {e}')
        return False

#добавление и обновление данных потерпевшего
def set_victim(full_name, birth_date, severity, protection_statuses):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("insert into victim(full_name, birth_date, severity, protection_statuses) values (%s, %s, %s, %s)", 
                           (full_name, birth_date, severity, protection_statuses))
            conn.commit()
            conn.close()
            return True
    except Exception as e:
        print(f'error: {e}')
        return False

def update_victim(victim_id, full_name, birth_date, severity, protection_statuses):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("update victim set full_name = %s, birth_date = %s, severity = %s, protection_statuses = %s where id = %s",
                           (full_name, birth_date, severity, protection_statuses, victim_id))
        if cursor.rowcount == 0:
            cursor.execute(
                "SELECT id FROM victim WHERE id = %s",
                (victim_id,)
            )

            if cursor.fetchone() is None:
                print(f"Дело с ID {victim_id} не найдено")
                return False
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'error: {e}')
        return False

#добавление и обновление данных потерпевшего
def set_witness(full_name, witness_reliability_levels, program_stages):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("insert into witness(full_name, witness_reliability_levels, program_stages) values (%s, %s, %s)", 
                           (full_name, witness_reliability_levels, program_stages))
            conn.commit()
            conn.close()
            return True
    except Exception as e:
        print(f'error: {e}')
        return False

def update_witness(witness_id, full_name, witness_reliability_levels, program_stages):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("update witness set full_name = %s, witness_reliability_levels = %s, program_stages = %s where id = %s",
                           (full_name, witness_reliability_levels, program_stages, witness_id))
        if cursor.rowcount == 0:
            cursor.execute(
                "SELECT id FROM witness WHERE id = %s",
                (witness_id,)
            )

            if cursor.fetchone() is None:
                print(f"Дело с ID {witness_id} не найдено")
                return False
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'error: {e}')
        return False

#добавление и обновление данных места преступления
def set_location(coordinates, address, district, object_type):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("insert into crime_location(coordinates, address, district, object_type) values (%s, %s, %s, %s)", 
                           (coordinates, address, district, object_type))
            conn.commit()
            conn.close()
            return True
    except Exception as e:
        print(f'error: {e}')
        return False

def update_location(location_id, coordinates, address, district, object_type):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("update crime_location set coordinates = %s, address = %s, district = %s, object_type = %s where id = %s",
                           (coordinates, address, district, object_type, location_id))
        if cursor.rowcount == 0:
            cursor.execute(
                "SELECT id FROM crime_location WHERE id = %s",
                (location_id,)
            )

            if cursor.fetchone() is None:
                print(f"Дело с ID {location_id} не найдено")
                return False
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f'error: {e}')
        return False

#удаление карточки и все связанные с ней данные
def delete_crime(crime_id):
    try:
        conn = get_db_connection()
        conn.begin()

        with conn.cursor() as cursor:
            # Получаем ID связанных уголовных дел и протоколов
            cursor.execute("""
                SELECT id, id_interrogation_record
                FROM criminal_case
                WHERE id_crime = %s
            """, (crime_id,))

            cases = cursor.fetchall()

            # Удаляем связь между преступлением и подозреваемым
            cursor.execute("""
                DELETE FROM suspect_crime
                WHERE id_crime = %s
            """, (crime_id,))

            # Удаляем улики, связанные с преступлением
            cursor.execute("""
                DELETE FROM clue
                WHERE id_crime = %s
            """, (crime_id,))

            # Удаляем уголовные дела
            cursor.execute("""
                DELETE FROM criminal_case
                WHERE id_crime = %s
            """, (crime_id,))

            # Удаляем протоколы, если они больше нигде не используются
            for case in cases:
                record_id = case[1]

                if record_id is not None:
                    cursor.execute("""
                        SELECT COUNT(*)
                        FROM criminal_case
                        WHERE id_interrogation_record = %s
                    """, (record_id,))

                    count = cursor.fetchone()[0]

                    if count == 0:
                        cursor.execute("""
                            DELETE FROM interrogation_record
                            WHERE id = %s
                        """, (record_id,))

        conn.commit()
        return True

    except Exception as e:
        if conn:
            conn.rollback()

        print(f"error: {e}")
        return False

    finally:
        if conn:
            conn.close()
