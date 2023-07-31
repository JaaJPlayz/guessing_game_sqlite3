import sqlite3

conn = sqlite3.connect("database/records.sqlite3")

c = conn.cursor()


def insert_record(name, attempts, wins, losses):
    c.execute(
        "INSERT INTO records (name, attempts, wins, losses) VALUES (?,?,?,?)",
        (name, attempts, wins, losses),
    )
    conn.commit()
    print("Record inserted successfully.")


def get_records():
    query_results = c.execute("SELECT * FROM records")
    records = query_results.fetchall()
    if not records:
        return "No records were found"
    return records


def get_record_by_id(rowid):
    c.execute("SELECT * FROM records WHERE rowid =?", (rowid,))
    return c.fetchone()


def get_record_by_name(name):
    c.execute("SELECT * FROM records WHERE name =?", (name,))
    return c.fetchone()


def update_record(name, attempts, wins, losses):
    c.execute(
        "UPDATE records SET attempts =?, wins =?, losses =? WHERE name =?",
        (attempts, wins, losses, name),
    )
    conn.commit()
    print("Record updated successfully.")


def delete_record(name):
    c.execute("DELETE FROM records WHERE name =?", (name,))
    conn.commit()
    print("Record deleted successfully.")


conn.close()
