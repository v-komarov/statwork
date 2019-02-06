import datetime
import time
import sys
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




def logpar(log):
    """Разбор строки лога"""


    data = {}
    data["call_a"] = log[20:32].strip()
    data["call_c"] = log[54:66].strip()
    data["duration"] = 0 if log[67:72].strip() == "" else int(log[67:72].strip(),10)

    data["in_out"] = True if len(data["call_a"]) > 4 and len(data["call_c"]) == 4 else False
    data["inner"] = True if len(data["call_a"]) == 4 and len(data["call_c"]) == 4 else False

    return data




#if __name__ == '__main__':

    """ Отладка формата входных данных """
#    with open("cdrlog.txt","r") as f:
#        lines = [line.rstrip() for line in f.readlines()]
#        for l in lines:
#            call_a = l[20:32].strip()
#            call_c = l[54:66].strip()
#            duration = 0 if l[67:72].strip() == "" else int(l[67:72].strip(),10)
#            print(l, call_a, call_c, duration)
#    sys.exit()




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
        
        if isInt(d["call_c"]) and isInt(d["call_a"]):
        
            session.execute("""INSERT INTO statwork.phone_log (id,source,datetime_call,year,month,day,call_a,call_b,call_c,duration,call_inner,in_out) 
                VALUES(UUID(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) USING TTL 31536000;""", 
                (conf.pref2,dt,year,month,day,d["call_a"],"",d["call_c"],d["duration"],d["inner"],d["in_out"]))



