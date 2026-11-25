import json
from datetime import datetime, timedelta
import dbconnect


def save_cache(cache_key, data, ttl=3600):
    conn = None

    try:
        conn = dbconnect.get_db_connection()

        expires_at = datetime.now() + timedelta(seconds=ttl)

        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO api_cache
                (cache_key, data, expires_at, status)
                VALUES (%s, %s, %s, 'active')
                ON DUPLICATE KEY UPDATE
                    data = VALUES(data),
                    updated_at = NOW(),
                    expires_at = VALUES(expires_at),
                    status = 'active'
            """, (
                cache_key,
                json.dumps(data, ensure_ascii=False),
                expires_at
            ))

        conn.commit()

    except Exception as e:
        print("Ошибка сохранения кеша:", e)

    finally:
        if conn:
            conn.close()

def get_cache(cache_key):
    conn = None

    try:
        conn = dbconnect.get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT data, expires_at, status
                FROM api_cache
                WHERE cache_key = %s
            """, (cache_key,))

            row = cursor.fetchone()

            if not row:
                return None

            data, expires_at, status = row

            if datetime.now() >= expires_at:
                return None

            if status != "active":
                return None

            return json.loads(data)

    except Exception as e:
        print("Ошибка получения кеша:", e)
        return None

    finally:
        if conn:
            conn.close()

def get_cache(cache_key):
    conn = None

    try:
        conn = dbconnect.get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT data, expires_at, status
                FROM api_cache
                WHERE cache_key = %s
            """, (cache_key,))

            row = cursor.fetchone()

            if not row:
                return None

            data, expires_at, status = row

            if datetime.now() >= expires_at:
                return None

            if status != "active":
                return None

            return json.loads(data)

    except Exception as e:
        print("Ошибка получения кеша:", e)
        return None

    finally:
        if conn:
            conn.close()

def cleanup_cache():
    conn = None

    try:
        conn = dbconnect.get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute("""
                DELETE FROM api_cache
                WHERE expires_at <= NOW()
            """)

        conn.commit()

    except Exception as e:
        print("Ошибка очистки кеша:", e)

    finally:
        if conn:
            conn.close()

def get_all_users():
    try:
        conn = dbconnect.get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("select user.id, user.login, role.name from user join role on user.id_role = role.id")
            roles = cursor.fetchall()
        return roles
    except Exception as e:
        print(f'error: {e}')