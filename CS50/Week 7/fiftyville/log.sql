-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Crime: July 28
-- Humphrey street
.schema
-- I have copied the schema to local vs code where I could reference it and aplit screen 3 ways so I can see all of them without scroling
select * from crime_scene_reports;
select description from crime_scene_reports where month = 7 and day = 28 and street = 'Humphrey Street';
-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
-- id  | year | month | day
-- 295 | 2025 | 7     | 28

select * from interviews where year = 2025 and month = 7 and day = 28 and transcript like '%bakery%';
-- Witnes 1 Ruth - 10:25am car left
-- Witnes 2 Eugene - Earliel in the morning ATM withdrawal at Leggett Street
-- Witnes 3 Raymond - Talk on the phone for less than a minute. Asking to book a flight for tomorrow

select * from atm_transactions where year = 2025 and month = 7 and day = 28 and atm_location = 'Leggett Street';
/*
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| id  | account_number | year | month | day |  atm_location  | transaction_type | amount |
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| 246 | 28500762       | 2025 | 7     | 28  | Leggett Street | withdraw         | 48     |
| 264 | 28296815       | 2025 | 7     | 28  | Leggett Street | withdraw         | 20     |
| 266 | 76054385       | 2025 | 7     | 28  | Leggett Street | withdraw         | 60     |
| 267 | 49610011       | 2025 | 7     | 28  | Leggett Street | withdraw         | 50     |
| 269 | 16153065       | 2025 | 7     | 28  | Leggett Street | withdraw         | 80     |
| 288 | 25506511       | 2025 | 7     | 28  | Leggett Street | withdraw         | 20     |
| 313 | 81061156       | 2025 | 7     | 28  | Leggett Street | withdraw         | 30     |
| 336 | 26013199       | 2025 | 7     | 28  | Leggett Street | withdraw         | 35     |
+-----+----------------+------+-------+-----+----------------+------------------+--------+
*/

select * from bakery_security_logs where year = 2025 and month = 7 and day = 28 and hour = 10 and minute > 20 and minute < 30;
/*
+-----+------+-------+-----+------+--------+----------+---------------+
| id  | year | month | day | hour | minute | activity | license_plate |
+-----+------+-------+-----+------+--------+----------+---------------+
| 265 | 2025 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
| 266 | 2025 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
| 267 | 2025 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
+-----+------+-------+-----+------+--------+----------+---------------+
*/
select * from people where license_plate in (select license_plate from bakery_security_logs where year = 2025 and month = 7 and day = 28 and hour = 10 and minute > 20 and minute < 30);
select * from phone_calls where year = 2025 and month = 7 and day = 28 and duration < 60;
/*
+-----+----------------+----------------+------+-------+-----+----------+
| id  |     caller     |    receiver    | year | month | day | duration |
+-----+----------------+----------------+------+-------+-----+----------+
| 221 | (130) 555-0289 | (996) 555-8899 | 2025 | 7     | 28  | 51       |
| 224 | (499) 555-9472 | (892) 555-8872 | 2025 | 7     | 28  | 36       |
| 233 | (367) 555-5533 | (375) 555-8161 | 2025 | 7     | 28  | 45       |
| 251 | (499) 555-9472 | (717) 555-1342 | 2025 | 7     | 28  | 50       |
| 254 | (286) 555-6063 | (676) 555-6554 | 2025 | 7     | 28  | 43       |
| 255 | (770) 555-1861 | (725) 555-3243 | 2025 | 7     | 28  | 49       |
| 261 | (031) 555-6622 | (910) 555-3251 | 2025 | 7     | 28  | 38       |
| 279 | (826) 555-1652 | (066) 555-9701 | 2025 | 7     | 28  | 55       |
| 281 | (338) 555-6650 | (704) 555-2131 | 2025 | 7     | 28  | 54       |
+-----+----------------+----------------+------+-------+-----+----------+
*/
select * from flights where year = 2025 and month = 7 and day = 29;
select * from airports where id in(select origin_airport_id from flights where year = 2025 and month = 7 and day = 29);
/*
╭────┬──────────────┬─────────────────────────────┬────────────╮
│ id │ abbreviation │          full_name          │    city    │
╞════╪══════════════╪═════════════════════════════╪════════════╡
│  8 │ CSF          │ Fiftyville Regional Airport │ Fiftyville │
╰────┴──────────────┴─────────────────────────────┴────────────╯
*/
select * from airports where id in(select destination_airport_id from flights where year = 2025 and month = 7 and day = 29);
/*
╭────┬──────────────┬─────────────────────────────────────┬───────────────╮
│ id │ abbreviation │              full_name              │     city      │
╞════╪══════════════╪═════════════════════════════════════╪═══════════════╡
│  1 │ ORD          │ O'Hare International Airport        │ Chicago       │
│  4 │ LGA          │ LaGuardia Airport                   │ New York City │
│  6 │ BOS          │ Logan International Airport         │ Boston        │
│  9 │ HND          │ Tokyo International Airport         │ Tokyo         │
│ 11 │ SFO          │ San Francisco International Airport │ San Francisco │
╰────┴──────────────┴─────────────────────────────────────┴───────────────╯
*/
select * from people where phone_number in 
(select caller from phone_calls where year = 2025 and month = 7 and day = 28 and duration < 60)
and license_plate in
(select license_plate from bakery_security_logs where year = 2025 and month = 7 and day = 28 and hour = 10 and minute > 20 and minute < 30)
/*
╭────────┬────────┬────────────────┬─────────────────┬───────────────╮
│   id   │  name  │  phone_number  │ passport_number │ license_plate │
╞════════╪════════╪════════════════╪═════════════════╪═══════════════╡
│ 514354 │ Diana  │ (770) 555-1861 │      3592750733 │ 322W7JE       │
│ 560886 │ Kelsey │ (499) 555-9472 │      8294398571 │ 0NTHK55       │
╰────────┴────────┴────────────────┴─────────────────┴───────────────╯
*/
select * from passengers where passport_number = '3592750733';
select * from flights where id in (select flight_id from passengers where passport_number = '3592750733');
/*
╭────┬───────────────────┬──────────────────────┬──────┬───────┬─────┬──────┬────────╮
│ id │ origin_airport_id │ destination_airpo... │ year │ month │ day │ hour │ minute │
╞════╪═══════════════════╪══════════════════════╪══════╪═══════╪═════╪══════╪════════╡
│ 18 │                 8 │                    6 │ 2025 │     7 │  29 │   16 │      0 │
│ 24 │                 7 │                    8 │ 2025 │     7 │  30 │   16 │     27 │
│ 54 │                 8 │                    5 │ 2025 │     7 │  30 │   10 │     19 │
╰────┴───────────────────┴──────────────────────┴──────┴───────┴─────┴──────┴────────╯
*/
select * from flights where id in (select flight_id from passengers where passport_number = '8294398571');
/*
We found our man
╭────┬───────────────────┬──────────────────────┬──────┬───────┬─────┬──────┬────────╮
│ id │ origin_airport_id │ destination_airpo... │ year │ month │ day │ hour │ minute │
╞════╪═══════════════════╪══════════════════════╪══════╪═══════╪═════╪══════╪════════╡
│ 36 │                 8 │                    4 │ 2025 │     7 │  29 │    8 │     20 │
╰────┴───────────────────┴──────────────────────┴──────┴───────┴─────┴──────┴────────╯
*/
select * from phone_calls where caller = '(499) 555-9472';
/*
╭─────┬────────────────┬────────────────┬──────┬───────┬─────┬──────────╮
│ id  │     caller     │    receiver    │ year │ month │ day │ duration │
╞═════╪════════════════╪════════════════╪══════╪═══════╪═════╪══════════╡
│  73 │ (499) 555-9472 │ (770) 555-1861 │ 2025 │     7 │  25 │      317 │
│ 224 │ (499) 555-9472 │ (892) 555-8872 │ 2025 │     7 │  28 │       36 │
│ 251 │ (499) 555-9472 │ (717) 555-1342 │ 2025 │     7 │  28 │       50 │
│ 424 │ (499) 555-9472 │ (996) 555-8899 │ 2025 │     7 │  30 │      506 │
│ 478 │ (499) 555-9472 │ (020) 555-6715 │ 2025 │     7 │  31 │      102 │
╰─────┴────────────────┴────────────────┴──────┴───────┴─────┴──────────╯
*/
select * from phone_calls where receiver = '(717) 555-1342';
select * from people where phone_number in ('(717) 555-1342', '(892) 555-8872');
/*
Accomplice is one of them:
╭────────┬─────────┬────────────────┬─────────────────┬───────────────╮
│   id   │  name   │  phone_number  │ passport_number │ license_plate │
╞════════╪═════════╪════════════════╪═════════════════╪═══════════════╡
│ 251693 │ Larry   │ (892) 555-8872 │      2312901747 │ O268ZZ0       │
│ 626361 │ Melissa │ (717) 555-1342 │      7834357192 │ NULL          │
╰────────┴─────────┴────────────────┴─────────────────┴───────────────╯
*/
select * from bank_accounts where person_id = '560886'
select flight_id from passengers where passport_number = '2312901747';
select flight_id from passengers where passport_number = '7834357192';

select * from flights where id = (select flight_id from passengers where passport_number = '2312901747');
select * from flights where id = (select flight_id from passengers where passport_number = '7834357192');
