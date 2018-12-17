## Компоненты для сбора CDR красноярских АТС

- **asterisk2cassandra.service** - реализация для systemd
- **avaya2cassandra.service** - реализация для systemd
- **cdr2cassandra_asterisk.py** - сервис загрузки CDR из топика kafka в cassandra хранилище
- **cdr2cassandra_avaya.py** - сервис загрузки CDR из топика kafka в cassandra хранилище
- **conf.py** - конфиг
