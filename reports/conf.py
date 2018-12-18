#coding:utf-8

"""Адрес cassandra кластера"""
ca_host = ['10.6.0.165',]
ca_port = 9042
ca_keyspace = "statwork"



"""Группы номеров телефонов"""
groups = ( 
    {"group": 1, "comment":"Alina Chernozubova",
        "phones": (
            { "source": "KRS-ASTERISK", "phones":(), "city":"КРАСНОЯРСК"},
            { "source": "KRS-G700", "phones":("1946","1961","1964","1934"), "city":"КРАСНОЯРСК"},
            { "source": "KRS-AVAYA", "phones":("1971","3745","1979","1948"), "city":"КРАСНОЯРСК"},
            { "source": "IRK-ASTERISK", "phones":("1121","1120","1123","1122","1124","5114","1644","1642","1643"), "city":"ИРКУТСК"},
            { "source": "CHI-ASTERISK", "phones":("4515","4505","4151","4401","5408","4516","1515"), "city":"ЧИТА"}
        ),

    },
)

