"""Tests for the RoomReady walking skeleton."""

import os
import tempfile

import pytest

import db


@pytest.fixture
def conn():
    """Create an in-memory database for each test."""
    c = db.connect(":memory:")
    db.init_db(c)
    db.seed_rooms(c)
    yield c
    c.close()


@pytest.fixture
def app(monkeypatch):
    """Build a Flask test client backed by the real app."""
    from app import create_app

    # Use a temp file so the app's module-level DB is not touched in tests.
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        db_path = tmp.name
    monkeypatch.setattr("app.DB_PATH", db_path)

    app = create_app()
    app.config["TESTING"] = True
    client = app.test_client()
    yield client
    os.unlink(db_path)


def test_rooms_are_seeded(conn):
    rooms = db.get_rooms(conn)
    assert len(rooms) == 3
    assert rooms[0]["name"] == "Standard Single"


def test_create_booking_saves(conn):
    booking_id = db.create_booking(conn, "Alice", 1, "2026-09-10", "2026-09-12")
    booking = db.get_booking(conn, booking_id)
    assert booking["guest_name"] == "Alice"
    assert booking["room_name"] == "Standard Single"
    assert booking["check_in"] == "2026-09-10"


def test_create_booking_unknown_room_raises(conn):
    with pytest.raises(ValueError):
        db.create_booking(conn, "Bob", 999, "2026-09-10", "2026-09-12")


def test_index_lists_rooms(app):
    response = app.get("/")
    assert response.status_code == 200
    body = response.get_data(as_text=True)
    assert "Deluxe King" in body
    assert "Standard Single" in body


def test_book_route_saves_and_redirects(app):
    response = app.post(
        "/book/1",
        data={
            "guest_name": "Alice",
            "check_in": "2026-09-10",
            "check_out": "2026-09-12",
        },
    )
    assert response.status_code == 302
    assert "/confirmation/" in response.headers["Location"]


def test_book_route_missing_fields_bad_request(app):
    response = app.post("/book/1", data={"guest_name": ""})
    assert response.status_code == 400


def test_book_route_unknown_room_not_found(app):
    response = app.post(
        "/book/999",
        data={
            "guest_name": "Bob",
            "check_in": "2026-09-10",
            "check_out": "2026-09-12",
        },
    )
    assert response.status_code == 404


def test_confirmation_shows_booking(app):
    booking = app.post(
        "/book/2",
        data={
            "guest_name": "Carol",
            "check_in": "2026-10-01",
            "check_out": "2026-10-03",
        },
    )
    location = booking.headers["Location"]
    response = app.get(location)
    body = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "Carol" in body
    assert "Double Room" in body


# --- Availability search ---


def test_all_rooms_available_when_no_bookings(conn):
    rooms = db.get_available_rooms(conn, "2026-09-10", "2026-09-12")
    assert {r["id"] for r in rooms} == {1, 2, 3}


def test_room_with_overlapping_booking_unavailable(conn):
    db.create_booking(conn, "Alice", 1, "2026-09-10", "2026-09-12")
    rooms = db.get_available_rooms(conn, "2026-09-11", "2026-09-13")
    ids = {r["id"] for r in rooms}
    assert 1 not in ids
    assert 2 in ids and 3 in ids


def test_room_free_on_existing_checkout_day(conn):
    db.create_booking(conn, "Alice", 1, "2026-09-10", "2026-09-12")
    rooms = db.get_available_rooms(conn, "2026-09-12", "2026-09-14")
    assert 1 in {r["id"] for r in rooms}


def test_request_ending_on_existing_checkin_day_available(conn):
    db.create_booking(conn, "Alice", 1, "2026-09-10", "2026-09-12")
    rooms = db.get_available_rooms(conn, "2026-09-08", "2026-09-10")
    assert 1 in {r["id"] for r in rooms}


def test_booking_only_blocks_its_own_room(conn):
    db.create_booking(conn, "Alice", 2, "2026-09-10", "2026-09-12")
    rooms = db.get_available_rooms(conn, "2026-09-11", "2026-09-13")
    ids = {r["id"] for r in rooms}
    assert 2 not in ids
    assert 1 in ids and 3 in ids


def test_index_with_dates_hides_booked_room(app):
    app.post(
        "/book/1",
        data={
            "guest_name": "Alice",
            "check_in": "2026-09-10",
            "check_out": "2026-09-12",
        },
    )
    response = app.get("/?check_in=2026-09-11&check_out=2026-09-13")
    body = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "Standard Single" not in body
    assert "Double Room" in body
    assert "Deluxe King" in body


# --- My bookings view ---


def test_get_bookings_returns_all_with_room_names(conn):
    db.create_booking(conn, "Alice", 1, "2026-09-10", "2026-09-12")
    db.create_booking(conn, "Bob", 2, "2026-09-20", "2026-09-22")
    bookings = db.get_bookings(conn)
    assert len(bookings) == 2
    assert bookings[0]["room_name"] == "Standard Single"
    assert bookings[-1]["room_name"] == "Double Room"
    assert bookings[0]["guest_name"] == "Alice"


def test_bookings_page_lists_all_bookings(app):
    app.post(
        "/book/1",
        data={
            "guest_name": "Alice",
            "check_in": "2026-09-10",
            "check_out": "2026-09-12",
        },
    )
    app.post(
        "/book/3",
        data={
            "guest_name": "Bob",
            "check_in": "2026-09-20",
            "check_out": "2026-09-22",
        },
    )
    response = app.get("/bookings")
    body = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "Alice" in body
    assert "Bob" in body
    assert "Standard Single" in body
    assert "Deluxe King" in body
    assert "2026-09-10" in body