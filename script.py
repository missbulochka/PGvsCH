#!/usr/bin/env python3

from clickhouse_driver import Client
import sys, psycopg2
import modules.pg as pg
import modules.ch as ch

DBNAME = "perfdb";
USER = "admin";
PASSWORD = "password";
HOST = "127.0.0.1";


if __name__ == "__main__":
    chConn = Client(HOST)
    pgConn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)

    if len(sys.argv) > 1:
        if sys.argv[1] == "migrate":
            pg.migrate(pgConn)
            ch.migrate(chConn)
        elif sys.argv[1] == "fill":
            pg.insert(pgConn)
            ch.insert(chConn)

    pgConn.commit()
    pgConn.close()
