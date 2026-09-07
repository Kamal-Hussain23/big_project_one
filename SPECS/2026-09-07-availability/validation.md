# Validation — Availability Search

## Success criteria

- On the home page a user can pick check-in and check-out dates and see only
  the rooms that are free for those dates.
- A room with a booking that overlaps the requested dates is hidden.
- A room whose existing booking ends on the requested check-in day is shown
  (check-out is departure day).
- With no dates chosen, all rooms are shown (unchanged behaviour).

## Verification steps

- [ ] Test suite all green.
- [ ] `ruff check` clean.
- [ ] Locally: create a booking, then `curl "/?check_in=...&check_out=..."` and
      confirm the booked room is hidden and the others shown.
- [ ] Public Codio URL responds.

## Spec drift check

- Compare against SPECS/ and this feature spec; surface differences to the user
  and update specs on approval.