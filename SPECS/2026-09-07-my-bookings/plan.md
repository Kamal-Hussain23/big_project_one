# Plan — My Bookings View

TDD note: this is a Red/Green repo. Write a failing test first, watch it fail,
then write the minimal code to make it pass.

## Task group 1 — Database: getting all bookings

- [ ] Write failing tests for `db.get_bookings`:
      - returns each booking joined with its room name;
      - returns them in booking order.
- [ ] Implement `get_bookings` in `db.py` and make tests pass (green).

## Task group 2 — The /bookings page

- [ ] Write a failing test: `GET /bookings` lists each booking's guest, room,
      and dates.
- [ ] Add the `/bookings` route in `app.py`.
- [ ] Add `templates/bookings.html`.
- [ ] Make tests pass (green).

## Task group 3 — Final checks

- [ ] Run the full test suite; all green.
- [ ] Run `ruff check`; no errors.
- [ ] Verify the server responds and `/bookings` works locally.