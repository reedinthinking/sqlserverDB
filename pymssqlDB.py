import pymssql

conn = pymssql.connect(host='192.168.1.5',user='sa',password='attnsunlike',database='db_001')
cur = conn.cursor()
cur.execute('select * from [dbo].accn')
rows = cur.fetchall()

for row in rows:
    print(row[1])

cur.close()
conn.close()