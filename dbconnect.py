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
            cursor.execute("select id, name, mini_description from crime where is_deleted = 0 order by name")
            crimes = cursor.fetchall()
        return crimes
    except Exception as e:
        print(f'error: {e}')

def get_username(user_id):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("select login from user where id = %s", (user_id,))
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

def get_investigator():
    try:
        conn = get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT id, full_name
                FROM investigator
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

#удаление карточки и все связанные с ней данные перманентно
def delete_crime(crime_id):
    try:
        conn = get_db_connection()
        conn.begin()

        with conn.cursor() as cursor:
            cursor.execute("""SELECT id, id_interrogation_record FROM criminal_case WHERE id_crime = %s""", (crime_id,))

            cases = cursor.fetchall()

            cursor.execute("""DELETE FROM suspect_crime WHERE id_crime = %s""", (crime_id,))

            cursor.execute("""DELETE FROM clue WHERE id_crime = %s""", (crime_id,))

            cursor.execute("""DELETE FROM criminal_case WHERE id_crime = %s""", (crime_id,))

            cursor.execute("""DELETE FROM crime WHERE id = %s""", (crime_id,))

            for case in cases:
                record_id = case[1]

                if record_id is not None:
                    cursor.execute("""SELECT COUNT(*) FROM criminal_case WHERE id_interrogation_record = %s""", (record_id,))

                    count = cursor.fetchone()[0]

                    if count == 0:
                        cursor.execute("""
                            DELETE FROM interrogation_record WHERE id = %s""", (record_id,))

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

# мягкое удаление в корзину
def soft_delete(crime_id):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("select id from crime where id = %s and is_deleted = 0", (crime_id, ))
            crime = cursor.fetchone()
            if crime is None:
                conn.rollback()
                return False
            
            cursor.execute("select id_interrogation_record from criminal_case where id_crime = %s and is_deleted = 0", (crime_id))
            records = cursor.fetchall()

            cursor.execute("update suspect_crime set is_deleted = 1, deleted_at = NOW(), deleted_by_crime_id = %s where id_crime = %s and is_deleted = 0",
                           (crime_id, crime_id))

            cursor.execute("update clue set is_deleted = 1, deleted_at = NOW(), deleted_by_crime_id = %s where id_crime = %s and is_deleted = 0",
                                       (crime_id, crime_id))

            cursor.execute("update criminal_case set is_deleted = 1, deleted_at = NOW(), deleted_by_crime_id = %s where id_crime = %s and is_deleted = 0",
                                                   (crime_id, crime_id))
            cursor.execute("""
                            UPDATE crime_location
                            JOIN crime ON crime.id_crime_location = crime_location.id
                            SET crime_location.is_deleted = 1,
                                crime_location.deleted_at = NOW(),
                                crime_location.deleted_by_crime_id = %s
                            WHERE crime.id = %s
                            AND crime_location.is_deleted = 0
                        """, (crime_id, crime_id))
            cursor.execute("update crime set is_deleted = 1, deleted_at = NOW() where id = %s and is_deleted = 0",
                                                               (crime_id))

            for record in records:
                record_id = record[0]

                if record_id is None:
                    continue
                cursor.execute("select count(*) from criminal_case where id_interrogation_record = %s and is_deleted = 0 and id_crime != %s",
                               (record_id, crime_id))
                count = cursor.fetchone()[0]

                if count == 0:
                    cursor.execute("update interrogation_record set is_deleted = 1, deleted_at = NOW(), deleted_by_crime_id = %s where id = %s and is_deleted = 0",
                                                                       (crime_id, record_id))
        conn.commit()
        return True
    except Exception as e:
        if conn:
            conn.rollback()
        print(f'error: {e}')
    finally:
        if conn:
            conn.close()

def get_cards_in_trash():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("select id, name, mini_description from crime where is_deleted = 1 order by deleted_at desc")
            return cursor.fetchall()
    except Exception as e:
        print(f'error: {e}')
        return []
    finally:
        if conn:
            conn.close()

#восстановление из корзины
def restore_crime_from_trash(crime_id):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("select id from crime where id = %s and is_deleted = 1", (crime_id, ))
            crime = cursor.fetchone()
            if crime is None:
                conn.rollback()
                return False
            
            cursor.execute("select id_interrogation_record from criminal_case where id_crime = %s and is_deleted = 1 AND deleted_by_crime_id = %s", (crime_id, crime_id))
            records = cursor.fetchall()

            cursor.execute("update suspect_crime set is_deleted = 0, deleted_at = null, deleted_by_crime_id = null where id_crime = %s and is_deleted = 1 AND deleted_by_crime_id = %s",
                            (crime_id, crime_id))

            cursor.execute("update clue set is_deleted = 0, deleted_at = null, deleted_by_crime_id = null where id_crime = %s and is_deleted = 1 AND deleted_by_crime_id = %s",
                                        (crime_id, crime_id))

            cursor.execute("update criminal_case set is_deleted = 0, deleted_at = null, deleted_by_crime_id = null where id_crime = %s and is_deleted = 1 AND deleted_by_crime_id = %s",
                                                    (crime_id, crime_id))
            for record in records:
                record_id = record[0]
                if record_id is not None:
                    cursor.execute("update interrogation_record set is_deleted = 0, deleted_at = null, deleted_by_crime_id = null where id = %s and is_deleted = 1 AND deleted_by_crime_id = %s",
                                                                                            (record_id, crime_id))
                    
            cursor.execute("""
                            UPDATE crime_location
                            JOIN crime ON crime.id_crime_location = crime_location.id
                            SET crime_location.is_deleted = 0,
                                crime_location.deleted_at = null,
                                crime_location.deleted_by_crime_id = null
                            WHERE crime.id = %s
                            AND crime_location.is_deleted = 1
                            AND deleted_by_crime_id = %s
                        """, (crime_id, crime_id))
            cursor.execute("update crime set is_deleted = 0, deleted_at = null where id = %s and is_deleted = 1",
                                                                (crime_id, ))
        conn.commit()
        return True
    except Exception as e:
        if conn:
            conn.rollback()
        print(f'error: {e}')
    finally:
        if conn:
            conn.close()

#фильтрация карточек
def filtered_data(date_from, date_to, crime_type, district, investigator_id, crime_status, suspect_name, suspect_status):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            query = "select distinct crime.id, crime.name, crime.mini_description from crime where crime.is_deleted = 0"
            params = []

            if date_from and date_to:
                query += " and date(crime.date) between %s and %s"
                params.extend([date_from, date_to])

            if crime_type is not None:
                query += " and crime.type = %s"
                params.append(crime_type)

            if district:
                query += " and exists (select 1 from crime_location cl where cl.id = crime.id_crime_location and cl.district like %s)"
                params.append(f"%{district}%")

            if investigator_id is not None:
                query += " and exists (select 1 from criminal_case cc where cc.id_crime = crime.id  and cc.id_investigator = %s and cc.is_deleted = 0)"
                params.append(investigator_id)

            if crime_status is not None:
                query += " and crime.status = %s"
                params.append(crime_status)

            if suspect_name is not None:
                query += " and exists (select 1 from suspect_crime sc where sc.id_crime = crime.id and sc.id_suspect = %s and sc.is_deleted = 0)"
                params.append(suspect_name)

            if suspect_status is not None:
                query += " and exists (select 1 from suspect_crime sc join suspect s on s.id = sc.id_suspect where sc.id_crime = crime.id and sc.is_deleted = 0 and s.status = %s)"
                params.append(suspect_status)

            query += " order by crime.name"
            cursor.execute(query, params)
            return cursor.fetchall()
        
    except Exception as e:
        print(f'error: {e}')
        return []

    finally:
        if conn:
            conn.close()

#поиск в живом времени
def live_search(search_text):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            query = "select id, name, mini_description from crime where is_deleted = 0 and (name like %s or mini_description like %s) order by name"
            search = f"%{search_text.strip()}%"

            cursor.execute(query, (search, search))
            return cursor.fetchall()
    except Exception as e:
            print(f'error: {e}')
            return []
    
    finally:
        if conn:
            conn.close()