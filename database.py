import os 
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "db","booking.db")
SCHEMA_PATH = os.path.join(BASE_DIR, "db","schema.sql")

def get_db_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    return conn

def init_database():
    conn = get_db_connection()
    try:
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            sql = f.read()

            conn.executescript(sql)
            conn.commit()
    finally:
                conn.close()

def get_booked_seat_number (showtime_id):
    conn = get_db_connection()
    try:
        cursor = conn.execute("SELECT seat_number FROM bookings")
        booked_seats = [row[0] for row in cursor.fetchall()]
        return booked_seats
    finally:
        conn.close()

          