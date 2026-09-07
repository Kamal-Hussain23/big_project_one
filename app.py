"""RoomReady Flask application.

A tiny hotel room booking app. Shows rooms and lets you book one.
"""

import functools
import logging
import os

from flask import Flask, abort, g, redirect, render_template, request, url_for

import db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("roomready")

PORT = 3000
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "roomready.db")


def log_action(func):
    """Logging helper, kept separate from business logic."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info("called %s with %s %s", func.__name__, args, kwargs)
        return result

    return wrapper


def get_db():
    """Open one database connection per request, stored on the app context."""
    if "db" not in g:
        g.db = db.connect(DB_PATH)
    return g.db


def create_app():
    """Build the Flask app and initialise the database."""
    app = Flask(__name__)

    # Set up the tables and sample rooms once, at startup.
    setup_conn = db.connect(DB_PATH)
    db.init_db(setup_conn)
    db.seed_rooms(setup_conn)
    setup_conn.close()

    @app.teardown_appcontext
    def close_db(exc):
        conn = g.pop("db", None)
        if conn is not None:
            conn.close()

    @app.route("/")
    def index():
        check_in = request.args.get("check_in", "").strip()
        check_out = request.args.get("check_out", "").strip()

        if check_in and check_out:
            rooms = db.get_available_rooms(get_db(), check_in, check_out)
        else:
            rooms = db.get_rooms(get_db())
            check_in = ""
            check_out = ""

        return render_template(
            "index.html",
            rooms=rooms,
            check_in=check_in,
            check_out=check_out,
        )

    @app.route("/bookings")
    def bookings():
        all_bookings = db.get_bookings(get_db())
        return render_template("bookings.html", bookings=all_bookings)

    @app.route("/book/<int:room_id>", methods=["POST"])
    @log_action
    def book(room_id):
        guest_name = request.form.get("guest_name", "").strip()
        check_in = request.form.get("check_in", "").strip()
        check_out = request.form.get("check_out", "").strip()

        if not guest_name or not check_in or not check_out:
            abort(400, "Please fill in your name and the dates.")

        try:
            booking_id = db.create_booking(
                get_db(), guest_name, room_id, check_in, check_out
            )
        except ValueError:
            abort(404, "Room not found")

        return redirect(url_for("confirmation", booking_id=booking_id))

    @app.route("/confirmation/<int:booking_id>")
    def confirmation(booking_id):
        booking = db.get_booking(get_db(), booking_id)
        if booking is None:
            abort(404, "Booking not found")
        return render_template("confirmation.html", booking=booking)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)