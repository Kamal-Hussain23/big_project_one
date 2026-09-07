# Requirements — My Bookings View

## Scope

Roadmap item 5: a simple view showing the bookings that have been made.

## Decisions

- **A new `/bookings` page** lists every booking: room name, guest name,
  check-in, check-out, and booking number.
- **Single-user local app** (see design.md Non-Goals), so no login and no
  filtering by user — just a flat list of all bookings.
- The existing `/confirmation/<id>` page is left unchanged.

## Files to change

- `db.py` — add a `get_bookings(conn)` helper returning all bookings joined
  with their room name, ordered by id.
- `app.py` — add the `/bookings` route rendering the list.
- `templates/bookings.html` — the list page.

## Out of scope

- Navigation links to the page (user chose "simple list").
- Editing, cancelling, or deleting bookings.
- Per-user filtering or login.

## Standards

- Follows the constitution and earlier feature specs: spec-driven development
  (code traces back to this spec), logging kept separate, simple and obvious
  solutions.