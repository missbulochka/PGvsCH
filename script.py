#!./venv/bin/python3
from clickhouse_driver import Client

import sys
import psycopg2
import pg_migrate_and_insertion
import ch_migrate_and_insertion

DBNAME = "postgres";
USER = "postgres";
PASSWORD = "amin111";
HOST = "127.0.0.1";

client = Client('localhost')




if __name__ == "__main__":

	#подключение, создание таблицы и заполнение 
    conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
    if len(sys.argv) > 1:
        if sys.argv[1] == "migrate":
            pg_migrate_and_insertion.migrate();
    pg_migrate_and_insertion.table_insert(conn);
    
    ch_migrate_and_insertion.migrate()
    for i in range(500):
        ch_migrate_and_insertion.insertion()

    conn.commit()
    conn.close()

