USE statwork;

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

