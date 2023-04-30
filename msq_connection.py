import mysql.connector
conn=mysql.connector.connect(host='',password='Gargi@5820', user='root')

if conn.is_connected():
	print('connection Established..')
	