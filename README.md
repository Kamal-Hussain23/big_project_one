# RoomReady

**Find a hotel room, check it's free, and book it — all in a few simple steps.**

RoomReady is a small hotel room booking app for travelers (tourists, business
people, and families). It exists because booking a hotel room can be confusing
and time-consuming. RoomReady keeps it simple and clear.

## The problem it solves

People struggle to find and book hotel rooms easily, especially when comparing
availability, prices, and dates across different options. Phoning a hotel or
wading through a confusing website just to know whether a room is free is slow
and frustrating.

## The solution

RoomReady shows you the rooms that exist, lets you pick your dates to see which
rooms are actually free, and lets you book one by typing your name and dates.
The booking is saved, and you get a clear confirmation. No accounts, no phone
calls, no fuss.

## Key features

- **Browse rooms** — every room with its name, price per night, and a short
  description.
- **Check availability** — pick check-in and check-out dates to see only the
  rooms that are free for those dates. The day you check out is free for the
  next guest (check-out is the departure day).
- **Book a room** — enter your name and dates and the booking is saved to the
  database.
- **Booking confirmation** — after booking you see a confirmation page with
  your room, dates, and booking number.
- **View all bookings** — the `/bookings` page lists every booking in a table.

## Tech stack

- **Frontend:** vanilla HTML, CSS, and a little vanilla JavaScript (used only
  to send the booking form without reloading the page).
- **Backend:** Python with Flask.
- **Database:** SQLite using Python's built-in `sqlite3` module. No ORM, no
  extra libraries.
- **Testing:** pytest. **Linting:** ruff.
- **Process:** Red/Green TDD — tests are written before the feature code.

## Database design

The database is small on purpose: two tables. A booking points at a room with
`room_id`, so one room can have many bookings over time.

```
Table: rooms
- id:          INTEGER PRIMARY KEY AUTOINCREMENT
- name:        TEXT     # the room name or number (e.g. "Deluxe King")
- price:       REAL     # the price per night
- description: TEXT     # a short description of the room
```

```
Table: bookings
- id:          INTEGER PRIMARY KEY AUTOINCREMENT
- guest_name:  TEXT     # the name of the person booking
- room_id:     INTEGER  # which room is booked (matches a room's id)
- check_in:    TEXT     # the first night's date (YYYY-MM-DD)
- check_out:   TEXT     # the departure day (YYYY-MM-DD)
```

Sample rooms seeded on first run: Standard Single (£60), Double Room (£90),
and Deluxe King (£130) per night.

To find free rooms for a date range, RoomReady asks the database for rooms
that have **no** booking that overlaps the requested dates. Two date ranges
overlap when each one starts before the other ends.

## Setup

1. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Start the server (already bound to `0.0.0.0`, port `3000`):
   ```
   python app.py
   ```
3. Open the public URL:
   `https://${CODIO_HOSTNAME}-3000.codio.io/`

## Run the tests

```
python -m pytest
python -m ruff check .
```

## What I Learned

Building RoomReady taught me a lot about going from "a vague idea" to a real
working app:

- **Think before you build.** We started by brainstorming three app ideas and
  writing down the problem, who experiences it, and why it matters. Choosing
  the hotel idea, we then wrote a short "constitution" (mission, tech rules,
  roadmap) and a feature spec *before* touching any code. Planning first made
  the code much easier to write.
- **The walking skeleton.** Instead of trying to build everything at once, we
  built the thinnest working slice first (a server that shows rooms and can
  book one), then grew features on top. Nothing sat around half-built.
- **Red/Green TDD.** Writing a failing test first, watching it fail, and then
  making it pass felt backward at first, but it meant every feature had a
  test proving it worked — and refactoring felt safe.
- **The weird SQLite threading bug.** The biggest surprise was a 500 error:
  SQLite connections created in one thread can only be used in that same
  thread. Flask serves each request on a different thread, so one shared
  connection broke. The fix was to open a connection per request using
  Flask's `g`. This taught me that "it works in my quick test" is not the
  same as "it works when the server really runs."
- **Coming up with the availability rule was the hardest part.** Finding free
  rooms looked easy, but getting the date-overlap logic right — and deciding
  that check-out day is free for the next guest — took careful thought and a
  few edge-case tests. Simple-looking features can hide tricky logic.
- **Saying no.** Writing explicit "non-goals" (no payments, no login, no
  export) kept the app small and finished. It's just as important to decide
  what you are *not* building.

## Project docs

- [SPECS/MISSION.md](SPECS/MISSION.md) — why this project exists and who it is for
- [SPECS/TECH.md](SPECS/TECH.md) — the tech stack and engineering standards
- [SPECS/ROADMAP.md](SPECS/ROADMAP.md) — current state, next steps, and vision

Feature details live in dated feature-spec folders under `SPECS/`, each with a
requirements, plan, and validation file.