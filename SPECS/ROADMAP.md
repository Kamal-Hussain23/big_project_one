# Roadmap

## Current state

We have the idea stage done: `design.md` records the project **RoomReady**, a
hotel room booking app, and its core problem. No code has been written yet.

## Next steps (in order)

1. Build a walking skeleton — the thinnest working slice: a Flask server that
   shows a page listing a few rooms and lets you book one.
2. Set up a simple SQLite database with a `rooms` table and a `bookings` table.
3. Add the search screen — show available rooms for chosen dates.
4. Add the booking flow — let a user reserve a room and see the booking saved.
5. Add a simple confirmation or "my bookings" view so a user can see what they
   reserved.

## Longer-term vision

Once the core booking works, keep it small and solid. Possible gentle additions
(only if they don't bloat the app): showing room details on a single page,
marking rooms as unavailable once booked, and a basic list of bookings.

The guiding rule: grow only with small, spec-approved steps on top of the
walking skeleton, never jumping ahead.
