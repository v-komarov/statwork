#coding:utf-8
import sys
import datetime
from cassandra.cluster import Cluster


import conf


cluster = Cluster(conf.ca_host,conf.ca_port)
session = cluster.connect()
session.set_keyspace(conf.ca_keyspace)


h4 = datetime.timedelta(hours=4)



def isInt(s):
    """Проверка строки на содержание чисел"""
    
    try:
        int(s)
        return True
    except:
        return False






def logpar(st):
    """Разбор строки лога"""

    data = {}
    duration = int(st[2],10) if isInt(st[2]) else 0
    data["duration"] = 0 if duration < 6 else duration # Длительность вызова в секундах

    data["call_a"] = (st[3])[2:] if len(st[3]) == 6 else st[3]
    data["call_b"] = ""
    data["call_c"] = (st[4])[2:] if len(st[4]) == 6 else st[4]
    data["in_out"] = True if data["call_c"] in conf.g700  else False
    data["inner"] = True if len(data["call_a"]) == 4 and len(data["call_c"]) else False

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
        st = line.split()
        if len(st) == 5:
            d = logpar(st)

            session.execute("""INSERT INTO statwork.phone_log (id,source,datetime_call,year,month,day,call_a,call_b,call_c,duration,call_inner,in_out)
                VALUES(UUID(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) USING TTL 31536000;""",
                (conf.pref,dt,year,month,day,d["call_a"],"",d["call_c"],d["duration"],d["inner"],d["in_out"]))
