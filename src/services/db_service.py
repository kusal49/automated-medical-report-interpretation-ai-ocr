import sqlite3
from pathlib import Path

DB_PATH = Path("data/health_reports.db")


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS blood_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT,
            report_name TEXT,
            extracted_text TEXT,
            analysis_result TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)


def save_report(user_email, report_name, extracted_text, analysis_result):
    with get_connection() as conn:
        conn.execute("""
        INSERT INTO blood_reports 
        (user_email, report_name, extracted_text, analysis_result)
        VALUES (?, ?, ?, ?)
        """, (user_email, report_name, extracted_text, analysis_result))


