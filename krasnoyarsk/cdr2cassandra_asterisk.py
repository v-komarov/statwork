#!/usr/bin/python
#coding:utf-8
import datetime
from cassandra.cluster import Cluster
from kafka import KafkaConsumer,TopicPartition
from netcat import Netcat



import conf


cluster = Cluster(conf.ca_host,conf.ca_port)
session = cluster.connect()
session.set_keyspace(conf.ca_keyspace)


nc = Netcat(conf.flume_krsk_asterisk['host'],conf.flume_krsk_asterisk['port'])




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
    log = log.replace("\"","").split(",")
    data["call_a"] = log[1]
    data["call_c"] = log[2]    
    mode = log[3]
    log.reverse()
    data["duration"] = int(log[4],10)

    data["in_out"] = True if len(data["call_a"]) > 4 and len(data["call_c"]) == 4 else False
    data["inner"] = True if len(data["call_a"]) == 4 and len(data["call_c"]) == 4 else False

    return data

consumer = KafkaConsumer(conf.ka_queue2,bootstrap_servers=conf.ka_host, auto_offset_reset='latest')

for m in consumer:

    cdr = m.value
    print cdr

    nc.write((cdr+'\n').encode("utf-8"))

    
    dt = datetime.datetime.now()
    day = dt.day
    month = dt.month
    year = dt.year
        
    d = logpar(cdr)
        
    if isInt(d["call_c"]):
        session.execute("""INSERT INTO statwork.phone_log (id,source,datetime_call,year,month,day,call_a,call_b,call_c,duration,call_inner,in_out) 
            VALUES(UUID(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) USING TTL 31536000;""", 
            (conf.pref2,dt,year,month,day,d["call_a"],"",d["call_c"],d["duration"],d["inner"],d["in_out"]))

    