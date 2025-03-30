import os
import psycopg2
import logging
from Entry import Entry
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")


def create_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        logging.error("Error connection to the database")
    return None


def get_cursor(connection):
    return connection.cursor()

def close_cursor_and_connection(connection,cursor):
    connection.close()
    cursor.close()
def commit_and_close(connection, cursor):
    connection.commit()
    close_cursor_and_connection(connection,cursor)
def rollback_and_close(connection,cursor):
    connection.rollback()
    close_cursor_and_connection(connection,cursor)
def create_new_entry(user_name, experiment_time, final_distance, experiment_type,
                     initial_speed, deceleration_of_front_car_stop_time,
                     initial_distance):
    connection = create_connection()
    cursor = get_cursor(connection)
    try:
        cursor.execute("""
            INSERT INTO entries (
                user_name,
                experiment_time,
                final_distance,
                experiment_type,
                initial_speed,
                deceleration_of_front_car_stop_time,
                initial_distance
            ) VALUES (%s, %s, %s, %s, %s, %s, %s);
        """, (
            user_name,
            experiment_time,
            final_distance,
            experiment_type,
            initial_speed,
            deceleration_of_front_car_stop_time,
            initial_distance
        ))
        commit_and_close(connection,cursor)
    except psycopg2.InternalError as e:
        rollback_and_close(connection,cursor)
        logging.warning(f"Error inserting entry: {e}")
        return False
    return True

def get_all_entries():
    connection = create_connection()
    cursor = get_cursor(connection)
    try:
        cursor.execute("SELECT user_name, experiment_time, final_distance, experiment_type, initial_speed, deceleration_of_front_car_stop_time, initial_distance FROM entries;")
        rows = cursor.fetchall()

        entries = []
        for row in rows:
            entry = Entry(
                user_name=row[0],
                experiment_time=row[1],
                final_distance=row[2],
                experiment_type=row[3],
                initial_speed=row[4],
                deceleration_of_front_car_stop_time=row[5],
                initial_distance=row[6]
            )
            entries.append(entry)
            close_cursor_and_connection(connection,cursor)
        return entries
    except psycopg2.InternalError as e:
        logging.warning(f"Error fetching entries: {e}")
        close_cursor_and_connection(connection,cursor)
        return []

