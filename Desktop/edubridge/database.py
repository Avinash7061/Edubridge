import sqlite3
from sqlite3 import Error

DATABASE_FILE = "edubridge.db"

def create_connection():
    """
    Creates a connection to the SQLite database.
    
    Returns:
        sqlite3.Connection: A connection object or None if an error occurs.
    """
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """
    Creates the 'progress' table if it doesn't already exist.
    This table will store student's quiz results.
    """
    try:
        sql_create_progress_table = """
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            lesson_id TEXT NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_progress_table)
    except Error as e:
        print(f"Error creating table: {e}")

def save_progress(conn, student_name, lesson_id, score, total):
    """
    Saves a student's quiz progress to the database.
    
    Args:
        conn (sqlite3.Connection): The database connection object.
        student_name (str): The name of the student.
        lesson_id (str): The ID of the completed lesson.
        score (int): The score the student achieved.
        total (int): The total possible score for the quiz.
    """
    sql = '''INSERT INTO progress(student_name, lesson_id, score, total)
             VALUES(?,?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (student_name, lesson_id, score, total))
        conn.commit()
    except Error as e:
        print(f"Error saving progress: {e}")

def setup_database():
    """
    A utility function to initialize the database and tables.
    """
    conn = create_connection()
    if conn is not None:
        create_table(conn)
        conn.close()
    else:
        print("Error! Cannot create the database connection.")