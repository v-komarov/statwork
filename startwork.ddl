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

