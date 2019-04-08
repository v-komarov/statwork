#coding:utf-8

"""Адрес cassandra кластера"""
ca_host = ['10.6.0.165',]
ca_port = 9042
ca_keyspace = "statwork"


"""Префикс"""
pref = "KRS-AVAYA"
pref2 = "KRS-ASTERISK"



"""kafka"""
ka_host = ["10.6.0.88:9092",]
ka_queue = "avaya"
ka_queue2 = "asterisk"


"""flume"""
flume_krsk_asterisk = {'host':'10.6.0.12','port':11126}
flume_krsk_avaya = {'host':'10.6.0.12','port':11124}

