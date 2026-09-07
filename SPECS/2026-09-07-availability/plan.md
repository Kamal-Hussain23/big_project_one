# Plan — Availability Search

Spec note: this is a spec-driven repo. Each task group comes from the
requirements in `requirements.md`; finish each group in order.

## Task group 1 — Database: getting free rooms

- [ ] Implement `db.get_available_rooms(conn, check_in, check_out)` so a room
      is free when no booking overlaps the requested dates (check-out is the
      departure day).

## Task group 2 — Home page search

- [ ] Update the `/` route in `app.py` to read the query params and filter.
- [ ] Add the date inputs + search control to `templates/index.html`.

## Task group 3 — Final checks

- [ ] Run `ruff check`; no errors.
- [ ] Verify the server responds and the search works locally.