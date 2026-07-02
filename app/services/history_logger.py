import sqlite3
from datetime import datetime

conn = sqlite3.connect("networking.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    event TEXT,
    topics TEXT,
    created_at TEXT
)
""")
conn.commit()


def save_history(name, event, topics):
    cursor.execute(
        "INSERT INTO history (name, event, topics, created_at) VALUES (?, ?, ?, ?)",
        (
            name,
            event,
            ", ".join(topics),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )
    conn.commit()