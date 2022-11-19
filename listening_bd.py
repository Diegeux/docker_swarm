import psycopg2

# Connect to existing database
conn = psycopg2.connect(
    database="base_dados",
    user="diego_igor",
    password="docker",
    host="192.168.99.107"
)

# Open cursor to perform database operation
cur = conn.cursor()

# Query the database 
cur.execute("SELECT * FROM docker_log")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close communications with database
cur.close()
conn.close()