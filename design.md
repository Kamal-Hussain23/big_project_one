# Project Brainstorming

## Idea 1
- **Problem:** People struggle to find and book hotel rooms easily, especially when comparing availability, prices, and dates across different options.
- **Who experiences this:** Travelers (tourists, business people, families) who need a simple way to search, compare, and reserve hotel rooms.
- **Why it matters:** Booking a hotel can be confusing and time-consuming. A simple, clean app makes planning trips easier and saves time.

## Idea 2
- **Problem:** Restaurants often get busy and people dislike waiting in line. It's hard to know if a table is available without calling.
- **Who experiences this:** People going out to eat who want to book a table ahead of time, and restaurant staff who manage reservations.
- **Why it matters:** It lets diners reserve a table without a phone call, and helps restaurants plan their seating better.

## Idea 3
- **Problem:** People want to attend concerts, movies, or events but often miss out because tickets sell out or are hard to buy.
- **Who experiences this:** People who want to find and buy tickets to local events, and the organizers who sell them.
- **Why it matters:** It makes ticketing easy and fair — buyers can search and reserve seats online, and organizers can track sales.

---

## Selected Project
- **App Name:** RoomReady
- **Target User:** Travelers (tourists, business people, families) who want to search and book hotel rooms.
- **Core Problem:** People struggle to find and book hotel rooms easily, especially when comparing availability, prices, and dates.
- **Purpose:** Provide a simple, clean way for users to search available rooms, see prices, and make reservations.

---

## Core Requirements
- As a traveler, I can see a list of all rooms with their name, price, and a short description.
- As a traveler, I can pick check-in and check-out dates and see only the rooms that are free (not already reserved) for those dates.
- As a traveler, I can book an available room by entering my name and dates, and the booking is saved.
- As a traveler, I can view the bookings that have been made (room, dates, guest name).

---

## Non-Goals
- No real payments or credit-card handling.
- No full hotel-management system for staff.
- No complicated search filters, reviews, loyalty programs, or password accounts.
- No user registration or login system (single-user local application).
- No mobile app or responsive mobile framework.
- No email or SMS notifications.
- No third-party API integrations.
- No export functionality (PDF, CSV, etc.).

---

## Database Questions

For each core requirement, write the specific question your database must be able to answer to make it work.

- Requirement 1 → Which rooms exist, and which ones are not already reserved for the chosen dates?
- Requirement 2 → How much does each room cost, and is it free to book?
- Requirement 3 → Does this booking save the room, the dates, and the guest name correctly?
- Requirement 4 → Which bookings exist and what details do they hold (room, dates, guest name)?

---

## Schema

```
Table: rooms
- id:          INTEGER PRIMARY KEY AUTOINCREMENT
- name:        TEXT     # the room name or number (e.g. "Deluxe King")
- price:       REAL     # the price per night
- description: TEXT     # a short description of the room
```

```
Table: bookings
- id:          INTEGER PRIMARY KEY AUTOINCREMENT
- guest_name:  TEXT     # the name of the person booking
- room_id:     INTEGER  # which room is booked (matches a room's id)
- check_in:    TEXT     # the first night's date
- check_out:   TEXT     # the last night's date
```
