# Requirements — Walking Skeleton

## Scope

The first item on ROADMAP.md: build the thinnest end-to-end slice of the
**RoomReady** app. Everything else in the roadmap grows on top of this.

For this feature we build:

- A Flask server bound to `0.0.0.0` on port `3000`.
- A running page (`/`) that lists a few hotel rooms.
- The ability to book one of those rooms.
- A booking confirmation shown to the user after booking.

## Decisions

- **SQLite now.** Even though ROADMAP lists database setup as a separate step,
  the user chose to set up SQLite (`rooms` and `bookings` tables) as part of
  this feature. Use Python's built-in `sqlite3` module. No ORMs.
- **Booking interaction uses a little vanilla JavaScript** on the page. No
  frameworks or libraries.
- **Branch:** `feature/walking-skeleton`.

## Context

- This is the first piece of code in the project; nothing exists yet.
- Single-user local application (see design.md Non-Goals) — no login system.
- Room availability by date is intentionally left for a later roadmap step. For
  this walking skeleton we only need to show rooms and book one.

## Schema (from design.md)

```
Table: rooms
- id:          INTEGER PRIMARY KEY AUTOINCREMENT
- name:        TEXT
- price:       REAL
- description: TEXT
```

```
Table: bookings
- id:          INTEGER PRIMARY KEY AUTOINCREMENT
- guest_name:  TEXT
- room_id:     INTEGER
- check_in:    TEXT
- check_out:   TEXT
```

## Out of scope

- Search/availability by date (roadmap item 3).
- Booking flow beyond a single simple booking (roadmap item 4).
- "My bookings" view (roadmap item 5).
- Real payments, logins, etc. (see design.md Non-Goals).

## Logging

- Feature follows the constitution: comprehensive logging, but kept separate
  from business logic (e.g. a small helper/decorator), not scattered through it.

## Contracts over parsing

- Use clear, defined data shapes and simple models rather than regex or string
  parsing to read room/booking data.
