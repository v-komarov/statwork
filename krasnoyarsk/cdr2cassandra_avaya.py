import datetime
import time
import sys
import json
from cassandra.cluster import Cluster

import conf


cluster = Cluster(conf.ca_host,conf.ca_port)
session = cluster.connect()
session.set_keyspace('pdrdata')



while True:
    line = sys.stdin.readline().strip()
    if line == "":
        break
    else:
        d = json.loads(line)
        epoch_minutes = int(d['camtime']//60)
        epoch_minutes = int(time.time()//60)
        session.execute("INSERT INTO pdrdata.recordspdr (id,camid,frame,epoch_minutes,data) VALUES(UUID(),%s,%s,%s,%s) USING TTL 86400;", (d['camid'],d['frame'],epoch_minutes,pickle.dumps(d)))



