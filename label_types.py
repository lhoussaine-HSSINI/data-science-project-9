import psycopg2


connection= psycopg2.connect(user='postgres', password='19980524', host='127.0.0.1', port='5432', database='employees_database')


cursor= connection.cursor()

cursor.execute("SELECT * from label_types")

ressult= cursor.fetchall()
ressult

cursor.execute("INSERT INTO label_types (label_id, Label_name, comments) values (%s, %s, %s)", ('1', 'positive', 'Positive feeling'))

cursor.execute("INSERT INTO label_types (label_id, Label_name, comments) values (%s, %s, %s)", ('0', 'negative', 'Negative feeling'))

cursor.execute("INSERT INTO label_types (label_id, Label_name, comments) values (%s, %s, %s)", ('2', 'neutral', 'Neutral feeling'))

cursor.execute("SELECT * from label_types")

ressult= cursor.fetchall()

ressult

len(ressult)