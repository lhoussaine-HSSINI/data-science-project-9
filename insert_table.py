
import numpy as np
import pandas as pd
import psycopg2 as  ps
from datetime import datetime

df= pd.read_csv('~/IMDB_Dataset.csv')

try:
        connection = ps.connect(user="postgres",
                                  password="19980524",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="employees_database")
        print("PostgreSQL connection is contacted")
        i=1
        for x in df['review']:
                now = datetime.now()
                d_t=now.strftime("%m-%d-%y")
                cursor = connection.cursor()
                postgreS_INSERT_1 = """INSERT INTO  data_input (id, text, date_inter_text) VALUES ( %s, %s, %s)"""
                val_insert_1 = (i, x, d_t)
                cursor.execute(postgreS_INSERT_1, val_insert_1)
                connection.commit()
                i+=1
        print("table data_input is inserted ")
        j=1
        for y in df['sentiment']:
                cursor = connection.cursor()
                postgreS_INSERT_2= """INSERT INTO  data_labeling (text_id, label_id, date_label) VALUES ( %s, %s, %s)"""
                if(y=='positive'):
                        k=1
                        now=datetime.now()
                        val_insert_2=(j, k, now)
                        cursor.execute(postgreS_INSERT_2, val_insert_2)
                        connection.commit()
                elif(y=='negative'):
                        k=0
                        now=datetime.now()
                        val_insert_2=(j, k, now)
                        cursor.execute(postgreS_INSERT_2, val_insert_2)
                        connection.commit()
                else:
                        k=2
                        now=datetime.now()
                        val_insert_2=(j, k, now)
                        cursor.execute(postgreS_INSERT_2, val_insert_2)
                        connection.commit()
                j+=1
        print("table data_labeling  is inserted ")
except (Exception, ps.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)
        connection.rollback()

finally:

        if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")


