# Tech

## Stack

The app uses only the simple tools the students already know:

- **Frontend:** vanilla HTML, CSS, and JavaScript. No React or other frameworks.
- **Backend:** Python with Flask.
- **Database:** SQLite, used in the simplest way (a few tables, no ORM). Data
  can also live in memory for the running app where that's easier.

## Architecture principles

- **Walking skeleton first.** Build the thinnest end-to-end slice of the app
  first (a server that shows a page and can book one room), then grow features
  on top of it. Prevents bloat.
- **Spec-driven development.** All work starts from a written spec
  (requirements/plan/validation). Code must trace back to an approved spec.
- **Simple over clever.** Prefer the most obvious, readable solution.
- **DRY (Don't Repeat Yourself).** If the same idea appears twice, pull it out
  into one shared piece rather than copying it.

## Engineering standards

- **Red/Green TDD.** Write a failing test first, watch it fail (red), then
  write the minimal code to make it pass (green), and clean up as needed.
- **Strict typing.** Use types where the language supports them and don't give
  up safety for convenience.
- **Contracts over custom logic.** Use clear, defined data shapes instead of
  hand-written parsing or messy string handling.
- **Separate logging from logic.** Keep the business code clean; add logging
  separately (e.g. with small helper functions) rather than scattering it
  through the middle of the logic.

## Rules

- Bind the server to `0.0.0.0`, never `127.0.0.1`.
- Use a port from 1024–9499 for HTTP (default `3000`).
- Announced URL: `https://${CODIO_HOSTNAME}-3000.codio.io/`.
