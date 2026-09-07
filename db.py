"""Database helpers for RoomReady.

Uses Python's built-in sqlite3 module. No ORM.
"""

import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS rooms (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT,
    price       REAL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS bookings (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    guest_name  TEXT,
    room_id     INTEGER,
    check_in    TEXT,
    check_out   TEXT
);
"""

SAMPLE_ROOMS = [
    ("Standard Single", 60.0, "A cosy single room with one bed."),
    ("Double Room", 90.0, "A comfortable room with a double bed."),
    ("Deluxe King", 130.0, "A large room with a king bed and a view."),
]


def connect(db_path):
    """Open a connection to the SQLite database at db_path."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(conn):
    """Create the rooms and bookings tables if they do not exist."""
    conn.executescript(SCHEMA)
    conn.commit()


def seed_rooms(conn):
    """Insert the sample rooms if the rooms table is empty."""
    count = conn.execute("SELECT COUNT(*) FROM rooms").fetchone()[0]
    if count == 0:
        conn.executemany(
            "INSERT INTO rooms (name, price, description) VALUES (?, ?, ?)",
            SAMPLE_ROOMS,
        )
        conn.commit()


def get_rooms(conn):
    """Return a list of all rooms."""
    return conn.execute("SELECT * FROM rooms ORDER BY id").fetchall()


def get_room(conn, room_id):
    """Return the room with the given id, or None if it does not exist."""
    return conn.execute("SELECT * FROM rooms WHERE id = ?", (room_id,)).fetchone()


def create_booking(conn, guest_name, room_id, check_in, check_out):
    """Save a booking and return its new id.

    Raises ValueError if the room does not exist.
    """
    room = get_room(conn, room_id)
    if room is None:
        raise ValueError("Room not found")
    cursor = conn.execute(
        "INSERT INTO bookings (guest_name, room_id, check_in, check_out) "
        "VALUES (?, ?, ?, ?)",
        (guest_name, room_id, check_in, check_out),
    )
    conn.commit()
    return cursor.lastrowid


def get_booking(conn, booking_id):
    """Return the booking with the given id joined with its room, or None."""
    return conn.execute(
        "SELECT b.id, b.guest_name, b.check_in, b.check_out, "
        "r.name AS room_name "
        "FROM bookings b JOIN rooms r ON b.room_id = r.id "
        "WHERE b.id = ?",
        (booking_id,),
    ).fetchone()


def get_bookings(conn):
    """Return all bookings joined with their room name, in booking order."""
    return conn.execute(
        "SELECT b.id, b.guest_name, b.check_in, b.check_out, "
        "r.name AS room_name "
        "FROM bookings b JOIN rooms r ON b.room_id = r.id "
        "ORDER BY b.id"
    ).fetchall()


def get_available_rooms(conn, check_in, check_out):
    """Return the rooms that have no booking overlapping the given dates.

    A booking occupies the nights from its check_in up to (but not including)
    its check_out. Two date ranges overlap when each starts before the other
    ends, so a room is free when no booking satisfies:

        booking.check_in <  check_out
        AND check_in < booking.check_out
    """
    return conn.execute(
        "SELECT * FROM rooms "
        "WHERE id NOT IN ("
        "    SELECT DISTINCT room_id FROM bookings "
        "    WHERE check_in < ? AND check_out > ?"
        ") "
        "ORDER BY id",
        (check_out, check_in),
    ).fetchall()