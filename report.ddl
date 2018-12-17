CREATE TABLE IF NOT EXISTS phone_report (
id uuid PRIMARY KEY,
mode text,
group int,
day int,
month int,
year int,
city text,
phone text,
calls int,
calls_out int,
calls_in int,
calls_out_ok,
calls_in_ok,
talk_out_avg int,
talk_in_avg int,
calls_out_per int,
calls_in_per int
);

CREATE INDEX IF NOT EXISTS ON phone_report (day);
CREATE INDEX IF NOT EXISTS ON phone_report (month);
CREATE INDEX IF NOT EXISTS ON phone_report (year);
CREATE INDEX IF NOT EXISTS ON phone_report (mode);
CREATE INDEX IF NOT EXISTS ON phone_report (group);

