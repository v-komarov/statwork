#!/usr/bin/python3.6
#coding:utf-8

import sys
import pandas as pd
import numpy as np
import datetime
from cassandra.cluster import Cluster

import conf


if __name__ != "__main__" or len(sys.argv) != 2:
    sys.exit()


mode = sys.argv[1] # Допустимые значания day month


cluster = Cluster(conf.ca_host,conf.ca_port)
session = cluster.connect()
session.set_keyspace(conf.ca_keyspace)


dt = datetime.datetime.today() - datetime.timedelta(days=1)

if mode == "day":
    query = "SELECT source,call_a,call_c,duration,in_out FROM phone_log WHERE day=%s AND month=%s AND year=%s ALLOW FILTERING;" % (dt.day, dt.month, dt.year)
elif mode == "month":
    query = "SELECT source,call_a,call_c,duration,in_out FROM phone_log WHERE month=%s AND year=%s ALLOW FILTERING;" % (dt.month, dt.year)
else:
    sys.exit()



df = pd.DataFrame(list(session.execute(query)),columns=["source","call_a","call_c","duration","in_out"])
df['call_a']= df['call_a'].astype(str)
df['call_c']= df['call_c'].astype(str)


for g in conf.groups:
    """По группам"""
    comment = g["comment"]
    group_id = g["group"]
    
    for p in g["phones"]:
        """По телефонам"""
        source = p["source"]
        city = p["city"]


        for t in p["phones"]:
            """По номерам телефонов"""
            df1 = df.loc[((df["call_a"]==t) | (df["call_c"]==t)) & (df["source"]==source)]
            calls = df1["source"].count() # Всего звонков по текущему номеру

            df2 = df1.loc[df1["in_out"] == True]
            calls_in = df2["call_c"].count() # Всего входящих
            df3 = df2.loc[df2["duration"] != 0]
            calls_in_ok = df3["call_c"].count() # Входящих принятых
            talk_in_avg = 0 if calls_in_ok == 0 else int(df3["duration"].mean()) # Средняя продолжительность разговора в сек
            calls_in_per = 0 if calls_in == 0 else calls_in_ok // calls_in * 100 # Проент принятых

            df2 = df1.loc[df1["in_out"] == False]
            calls_out = df2["call_a"].count() # Всего исходящих
            df3 = df2.loc[df2["duration"] != 0]
            calls_out_ok = df3["call_a"].count() # Исходящих принятых
            talk_out_avg = 0 if calls_out_ok == 0 else int(df3["duration"].mean()) # Средняя продолжительность разговора в сек
            calls_out_per = 0 if calls_out == 0 else calls_out_ok // calls_out * 100 # Проент принятых


            session.execute("""INSERT INTO statwork.phone_report (id,phone,group,city,calls,calls_in,calls_out,calls_in_ok,calls_out_ok,talk_in_avg,talk_out_avg,calls_in_per,calls_out_per, mode,day,month,year) 
                VALUES(UUID(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) USING TTL 2592000;""", 
                (t, group_id, city, calls, calls_in, calls_out, calls_in_ok, calls_out_ok, talk_in_avg, talk_out_avg, calls_in_per, calls_out_per, mode, dt.day, dt.month, dt.year))
