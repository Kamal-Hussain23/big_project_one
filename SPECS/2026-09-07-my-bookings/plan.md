# Plan — My Bookings View

Spec note: this is a spec-driven repo. Each task group comes from the
requirements in `requirements.md`; finish each group in order.

## Task group 1 — Database: getting all bookings

- [ ] Implement `db.get_bookings(conn)` so it returns each booking joined with
      its room name, in booking order.

## Task group 2 — The /bookings page

- [ ] Add the `/bookings` route in `app.py`.
- [ ] Add `templates/bookings.html`.

## Task group 3 — Final checks

- [ ] Run `ruff check`; no errors.
- [ ] Verify the server responds and `/bookings` works locally.