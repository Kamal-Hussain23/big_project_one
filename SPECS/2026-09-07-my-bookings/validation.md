# Validation — My Bookings View

## Success criteria

- Visiting `/bookings` shows every saved booking.
- Each row shows the room name, guest name, check-in, check-out, and booking
  number.
- Works with zero, one, or many bookings.

## Verification steps

- [ ] Test suite all green.
- [ ] `ruff check` clean.
- [ ] Locally: create a booking, `curl /bookings`, confirm it appears.
- [ ] Public Codio URL responds.

## Spec drift check

- Compare against SPECS/ and this feature spec; surface differences to the user
  and update specs on approval.