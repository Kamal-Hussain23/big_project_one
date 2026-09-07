# Plan — Walking Skeleton

Spec note: this is a spec-driven repo. Each task group below comes from the
requirements in `requirements.md`; finish each group in order.

## Task group 1 — Project setup

- [ ] Install `flask` (note it in a `requirements.txt`).
- [ ] Confirm the app can import and start without error.

## Task group 2 — Database setup (SQLite)

- [ ] Create helper to open/initialize the SQLite database with `rooms` and
      `bookings` tables (matching design.md schema).
- [ ] Seed a few sample rooms so the page has something to show.

## Task group 3 — Show rooms

- [ ] Add the Flask route that reads rooms from the database and renders them,
      per the requirements.

## Task group 4 — Book a room

- [ ] Add the booking route (POST) that inserts into `bookings` and redirects
      to the confirmation view, per the requirements.

## Task group 5 — Booking interaction (vanilla JS) + confirmation

- [ ] Add a minimal confirmation page.
- [ ] Add the small vanilla JS that wires the book button to the booking route.

## Task group 6 — Logging + final checks

- [ ] Add comprehensive logging via a small helper, kept separate from business
      logic.
- [ ] Run the lint checks; fix issues.
- [ ] Verify the server comes up and the page responds locally.