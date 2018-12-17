#!/usr/bin/python
#coding:utf-8
import datetime
from cassandra.cluster import Cluster


import conf


cluster = Cluster(conf.ca_host,conf.ca_port)
session = cluster.connect()
session.set_keyspace(conf.ca_keyspace)


h4 = datetime.timedelta(hours=4)


def logpar(log):
    """Разбор строки лога"""

    data = {}
    st = log.split(",")
    duration_str = st[1].split(":")
    h = int(duration_str[0],10)
    m = int(duration_str[1],10)
    s = int(duration_str[2],10)

    sec = datetime.timedelta(hours=h, minutes=m, seconds=s)
    
    data["call_a"] = st[3]
    data["call_b"] = st[6]
    data["call_c"] = st[5]
    data["duration"] = int(sec.total_seconds())
    data["in_out"] = True if st[4] == "I" else False
    data["inner"] = True if st[8] == "1" else False

    return data




while True:
    line = sys.stdin.readline().strip()
    if line == "":
        break
    else:
        dt = datetime.datetime.now() + h4
        day = dt.day
        month = dt.month
        year = dt.year
        d = logpar(line)

        session.execute("""INSERT INTO statwork.phone_log (id,source,datetime_call,year,month,day,call_a,call_b,call_c,duration,call_inner,in_out)
            VALUES(UUID(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) USING TTL 31536000;""",
            (conf.pref,dt,year,month,day,d["call_a"],"",d["call_c"],d["duration"],d["inner"],d["in_out"]))
