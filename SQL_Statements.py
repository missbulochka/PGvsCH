#!./venv/bin/python3
import psycopg2
import time
from diogram import Graph
from clickhouse_driver import Client

DBNAME = "postgres";
USER = "postgres";
PASSWORD = "amin111";
HOST = "127.0.0.1";

client = Client('localhost')

def analiz(a):
    max = a[0];
    min = a[0];
    s = 0;
    for i in range(len(a)):
        if(max<a[i]):
            max  = a[i];
        if(min>a[i]):
            min = a[i];
        s = s + a[i];
    return [min,s/len(a),max];


def pg_select(conn,i):
	t = [];
	try:
		file = open('SQL/test{}.sql'.format(i+1), encoding='utf-8')
		s = file.read();
		for j in range(10):
			cursor = conn.cursor();
			start_time = time.time();
			cursor.execute(s);
			#print("--- %s seconds ---" % (time.time() - start_time))
			t.append(time.time() - start_time);	
		t = analiz(t);
	except Exception as _ex:
		print ("[INFO] Error while working with PostgreSQL",_ex);
	finally:
		if conn:
			cursor.close();
			print("[INFO] PostgreSQL connection closed");
			return t;


def ch_select(i):
	t = [];
	try:
		file = open('SQL/test{}.sql'.format(i+1), encoding='utf-8')
		s = file.read();
		for j in range(10):
			start_time = time.time();
			client.execute(s);
			#print("--- %s seconds ---" % (time.time() - start_time))
			t.append(time.time() - start_time);	
		t = analiz(t);
	except Exception as _ex:
		print ("[INFO] Error ",_ex);
	finally:
		if client:
			return t;



if __name__ == "__main__": 
    conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)	

    postgres_time = [];
    ch_time = [];

    for i in range(10):
        postgres_time.append(pg_select(conn,i));
        ch_time.append(ch_select(i));

    rects_values = [[postgres_time],[ch_time]];
    graph = Graph(rects_values)
    graph.create_graph()
    conn.commit()
    conn.close()