# Plan — Availability Search

TDD note: this is a Red/Green repo. Write a failing test first, watch it fail,
then write the minimal code to make it pass.

## Task group 1 — Database: getting free rooms

- [ ] Write failing tests for `db.get_available_rooms`:
      - no bookings → all rooms available;
      - a booking on a room makes it unavailable for an overlapping request;
      - a request starting on the departure day of an existing booking IS
        available (check-out is departure day);
      - a booking on one room does not affect another room.
- [ ] Implement `get_available_rooms` in `db.py` and make tests pass (green).

## Task group 2 — Home page search

- [ ] Write a failing test: `GET /?check_in=...&check_out=...` shows only the
      rooms free for those dates.
- [ ] Update the `/` route in `app.py` to read the query params and filter.
- [ ] Add the date inputs + search control to `templates/index.html`.
- [ ] Make tests pass (green).

## Task group 3 — Final checks

- [ ] Run the full test suite; all green.
- [ ] Run `ruff check`; no errors.
- [ ] Verify the server responds and the search works locally.