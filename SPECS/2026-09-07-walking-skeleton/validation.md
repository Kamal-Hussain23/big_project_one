# Validation — Walking Skeleton

## How we know this feature is done and correct

- The Flask server starts successfully bound to `0.0.0.0` on port `3000`.
- The `/` page lists at least the seeded sample rooms with their name, price,
  and description.
- A user can book a room, and the booking is saved to the SQLite `bookings`
  table.
- After booking, the user sees a confirmation showing the saved booking
  (room, guest name, dates).
- The implementation matches this spec (spec-driven development).

## Verification steps

- [ ] Run lint (if configured); no errors.
- [ ] Start the server and verify `/` responds locally via `curl` to
      `http://localhost:3000/`.
- [ ] Verify the public Codio URL responds:
      `https://${CODIO_HOSTNAME}-3000.codio.io/`

## Spec drift check

- Compare the implemented code against SPECS/ (`MISSION.md`, `TECH.md`,
  `ROADMAP.md`) and this feature spec.
- Surface any differences to the user and, on their approval, update the
  relevant spec files.

## Merge criteria

- [ ] All checks above pass.
- [ ] Spec drift (if any) approved by the user and specs updated.
- [ ] Feature is merged to the main branch.
