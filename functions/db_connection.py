import yaml
import psycopg2
import pandas

def db_connect():
    with open("data/credentials.yaml", "r") as stream:
        try:
            credentials = yaml.safe_load(stream)['quero_collab']
        except yaml.YAMLError as exc:
            print(exc)

    conn = psycopg2.connect(
        host=credentials['host'],
        database=credentials['database'],
        user=credentials['user'],
        password=credentials['password'],
        port=credentials['port']
    )

    return conn

def db_consume(conn, query):
    
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        
        response = cursor.fetchall()
        
        cursor.close()
        return response
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    
def db_insert(conn, sql, values):    
    try:
        cursor = conn.cursor()
        cursor.executemany(sql, values)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)