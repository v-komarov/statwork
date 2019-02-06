USE statwork;

DROP TABLE phone_log;

CREATE TABLE IF NOT EXISTS phone_log (
id uuid, PRIMARY KEY,
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
call_inner boolean,
PRIMARY KEY (source,day,month,year)
) WITH CLUSTERING ORDER BY (year ASC, month ASC, day ASC);


CREATE INDEX IF NOT EXISTS ON phone_log (source);
CREATE INDEX IF NOT EXISTS ON phone_log (day);
CREATE INDEX IF NOT EXISTS ON phone_log (month);
CREATE INDEX IF NOT EXISTS ON phone_log (year);
CREATE INDEX IF NOT EXISTS ON phone_log (call_a);
CREATE INDEX IF NOT EXISTS ON phone_log (call_b);

