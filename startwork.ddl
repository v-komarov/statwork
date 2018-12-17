CREATE KEYSPACE IF NOT EXISTS statwork WITH replication = {'class':'SimpleStrategy', 'replication_factor':3};

CREATE TABLE IF NOT EXISTS phone_log (
id uuid PRIMARY KEY,
source varchar,
datetime_call timestamp,
day int,
month int,
year int,
duration int,
in_out boolean,
call_a varchar,
call_b varchar,
call_c varchar,
call_inner boolean
);

CREATE INDEX IF NOT EXISTS ON phone_log (source);
CREATE INDEX IF NOT EXISTS ON phone_log (day);
CREATE INDEX IF NOT EXISTS ON phone_log (month);
CREATE INDEX IF NOT EXISTS ON phone_log (year);
CREATE INDEX IF NOT EXISTS ON phone_log (call_a);
CREATE INDEX IF NOT EXISTS ON phone_log (call_b);
CREATE INDEX IF NOT EXISTS ON phone_log (in_out);
CREATE INDEX IF NOT EXISTS ON phone_log (call_inner);

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

