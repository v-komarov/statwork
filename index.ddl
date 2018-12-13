USE statwork;

CREATE INDEX IF NOT EXISTS ON phone_log (source);
CREATE INDEX IF NOT EXISTS ON phone_log (day);
CREATE INDEX IF NOT EXISTS ON phone_log (month);
CREATE INDEX IF NOT EXISTS ON phone_log (year);
CREATE INDEX IF NOT EXISTS ON phone_log (call_a);
CREATE INDEX IF NOT EXISTS ON phone_log (call_b);
CREATE INDEX IF NOT EXISTS ON phone_log (in_out);
CREATE INDEX IF NOT EXISTS ON phone_log (call_inner);

