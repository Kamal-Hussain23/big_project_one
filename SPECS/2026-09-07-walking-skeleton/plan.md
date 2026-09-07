# Plan — Walking Skeleton

TDD note: this is a Red/Green repo. Write a failing test first, watch it fail,
then write the minimal code to make it pass. Run tests after each task group.

## Task group 1 — Project setup

- [ ] Install `flask` (note it in a `requirements.txt`).
- [ ] Confirm the app can import and start without error.
- [ ] Run any project checks (tests) to establish a green baseline.

## Task group 2 — Database setup (SQLite)

- [ ] Create helper to open/initialize the SQLite database with `rooms` and
      `bookings` tables (matching design.md schema).
- [ ] Seed a few sample rooms so the page has something to show.
- [ ] Write a failing test for the DB helper, then make it pass.

## Task group 3 — Show rooms

- [ ] Write a failing test that the `/` page lists the room names/prices.
- [ ] Add the Flask route that reads rooms from the database and renders them.
- [ ] Make the test pass (green).

## Task group 4 — Book a room

- [ ] Write a failing test that booking a room saves a booking and returns a
      confirmation/reads back the booking.
- [ ] Add the booking route (POST) that inserts into `bookings`.
- [ ] Make the test pass (green).

## Task group 5 — Booking interaction (vanilla JS) + confirmation

- [ ] Write a failing test (where feasible) for the confirmation view showing
      the saved booking.
- [ ] Add a minimal confirmation page.
- [ ] Add the small vanilla JS that wires the book button to the booking route.
- [ ] Make tests pass.

## Task group 6 — Logging + final checks

- [ ] Add comprehensive logging via a small helper, kept separate from business
      logic.
- [ ] Run the full test suite; make sure everything is green.
- [ ] Run any lint checks; fix issues.
- [ ] Verify the server comes up and the page responds locally.
