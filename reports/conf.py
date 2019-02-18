#coding:utf-8

"""Адрес cassandra кластера"""
ca_host = ['10.6.0.165',]
ca_port = 9042
ca_keyspace = "statwork"



"""Группы номеров телефонов"""
groups = ( 
    {"group": 1, "comment":"Alina Chernozubova",
        "phones": (
            { "source": "KRS-ASTERISK", "phones":("1948",), "city":"КРАСНОЯРСК"},
            { "source": "KRS-G700", "phones":("1946","1961","1964","1934"), "city":"КРАСНОЯРСК"},
            { "source": "KRS-AVAYA", "phones":("1971","3745","1979"), "city":"КРАСНОЯРСК"},
            { "source": "IRK-ASTERISK", "phones":("1121","1120","1123","1122","1124","1644","1642","1643"), "city":"ИРКУТСК"},
            { "source": "UU-ASTERISK", "phones":("5114",), "city":"УЛАН-УДЭ"},
            { "source": "CHI-ASTERISK", "phones":("4515","4505","4151","4508","4516"), "city":"ЧИТА"},
            { "source": "CHI-DEFINITY", "phones":("1515",), "city":"ЧИТА"}
        ),

    },
    {"group": 2, "comment":"Ludmila Kuricyna",
        "phones": (
            { "source": "KRS-ASTERISK", "phones":(), "city":"КРАСНОЯРСК"},
            { "source": "KRS-G700", "phones":("1985","1981","1974"), "city":"КРАСНОЯРСК"},
            { "source": "KRS-G700", "phones":("3746","3743","1941"), "city":"АБАКАН"},
            { "source": "KRS-AVAYA", "phones":("1911",), "city":"АБАКАН"},
            { "source": "KRS-AVAYA", "phones":("1982","1989"), "city":"АЧИНСК"},
            { "source": "KRS-AVAYA", "phones":("1976",), "city":"НАЗАРОВО"},
            { "source": "KRS-G700", "phones":("3668","1949"), "city":"ДИВНОГОРСК"},
            { "source": "KRS-AVAYA", "phones":("1914",), "city":"МИНУСИНСК"},
            { "source": "KRS-AVAYA", "phones":("1935",), "city":"ЗЕЛЕНОГОРСК"},
            { "source": "KRS-AVAYA", "phones":("4726","4730"), "city":"ЛЕСОСИБИРСК"},
            { "source": "IRK-ASTERISK", "phones":("1624","1625","1543","1626","1622"), "city":"ИРКУТСК"},
            { "source": "IRK-ASTERISK", "phones":("5402","5401"), "city":"УСОЛЬЕ-СИБИРСКОЕ"},
            { "source": "ANG-ASTERISK", "phones":("3502","3504"), "city":"АНГАРСК"},
            { "source": "ZHI-ASTERISK", "phones":("5840",), "city":"ЖЕЛЕЗНОГОРСК-ИЛИМСКИЙ"},
            { "source": "UU-ASTERISK", "phones":("5113","5115","5112"), "city":"УЛАН-УДЭ"},
            { "source": "CHI-ASTERISK", "phones":("4405","4402","4411","4555","4408","4403","4420"), "city":"ЧИТА"},
            { "source": "CHI-ASTERISK", "phones":("4122",), "city":"КРАСНОКАМЕНСК"},
            { "source": "CHI-ASTERISK", "phones":("4096",), "city":"БЕЛОГОРСК"},
            { "source": "CHI-ASTERISK", "phones":("4103",), "city":"ЯСНОГОРСК"},
            { "source": "CHI-ASTERISK", "phones":("4098",), "city":"СВОБОДНЫЙ"},
            { "source": "CHI-ASTERISK", "phones":("4157",), "city":"БЛАГОВЕЩЕНСК"},
            { "source": "SBA-ASTERISK", "phones":("5851",), "city":"СЕВЕРОБАЙКАЛЬСК"},
            { "source": "GOZ-ASTERISK", "phones":("5871",), "city":"ГУСИНООЗЕРСК"},
            { "source": "CHI-DEFINITY", "phones":(), "city":"ЧИТА"}
        ),

    },
    {"group": 3, "comment":"Olga Malikova",
        "phones": (
            { "source": "IRK-ASTERISK", "phones":("1621","1542"), "city":"ИРКУТСК"},
        ),

    },

)

