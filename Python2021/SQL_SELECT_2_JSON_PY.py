# QUERY SQL AND RESPOND IN JSON
import pyodbc
import json
import collections
servername = 'xxxxxxxxx'
database = 'xxxxxxxx'
username = 'xxxxxxxxx'
password = 'xxxxxxxxxx'     
driver= '{ODBC Driver 13 for SQL Server}'

connectionstr = 'DRIVER=' + driver + ';Server=tcp:' + servername + '.database.windows.net,1433;Database=' + database + ';Uid=' + username + ';Pwd=' + password + ';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'

with pyodbc.connect(connectionstr) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM [dbo].[Mytable]")
        rows = cursor.fetchall()
        #print("All rows : " + str(rows))
        rowarray_list = []
        for row in rows:
            #print ("Each row : " + str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " "  + str(row[3]))
            t = (row[0], row[1], row[2], row[3])
            rowarray_list.append(t)

j = json.dumps(rowarray_list)
#print("Pure Json dumps : " + j)

# Convert query to objects of key-value pairs
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d["id"] = row[0]
    d["firstName"] = row[1]
    d["lastName"] = row[2]
    d["email"] = row[3]
    objects_list.append(d)
j = json.dumps(objects_list)
print(j)
conn.close()