# Requirements — Availability Search

## Scope

Roadmap item 3: let the traveler pick check-in and check-out dates and see only
the rooms that are free for those dates.

## Decisions

- **Dates live on the home page.** The home page (`/`) also offers two date
  inputs (check-in and check-out). Submitting them reloads the home page with
  the dates as query parameters and shows only the rooms that are free for
  those dates. No dates chosen = show all rooms (current behaviour).
- **Check-out is the departure day.** A booking occupies the nights from
  check-in up to (but not including) check-out. Example: a booking of
  `2026-09-10` to `2026-09-12` occupies the nights of the 10th and the 11th,
  so the room is free to book again starting the 12th.
- Dates stay as TEXT in `YYYY-MM-DD` format, so string comparison is correct.

## Availability rule

A room is **free** for a requested `check_in`/`check_out` if no existing
booking overlaps it. Two date ranges overlap when:

```
existing.check_in <  requested.check_out
AND requested.check_in < existing.check_out
```

## Files to change

- `db.py` — add a `get_available_rooms(conn, check_in, check_out)` helper.
- `app.py` — the `/` route reads `check_in`/`check_out` query params and
  filters the room list.
- `templates/index.html` — add the date inputs and a search control.

## Out of scope

- Building a separate search page/URL.
- Price filtering, room-type filters, etc. (see design.md Non-Goals).
- Any booking action changing (already covered by the walking skeleton).

## Standards

- Follows the constitution and the walking-skeleton feature spec: TDD
  (tests before code), logging kept separate, simple and obvious solutions.