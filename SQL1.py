# INSERT MULTIPLE ROWS INTO A SQL
import pyodbc
import json
from random import randrange
import random
import names
from datetime import datetime
from datetime import timedelta
import uuid

servername = 'xxxxxxxxx'
database = 'xxxxxxxx'
username = 'xxxxxxxxx'
password = 'xxxxxxxxxx'   
driver= '{ODBC Driver 13 for SQL Server}'
no_of_rows = 10
d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')

connectionstr = 'DRIVER=' + driver + ';Server=tcp:' + servername + '.database.windows.net,1433;Database=' + database + ';Uid=' + username + ';Pwd=' + password + ';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'

conn = pyodbc.connect(connectionstr)
def insert_row(insert_sql):
    cursor = conn.cursor()
    cursor.execute(insert_sql)
    conn.commit()

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def generate_random_data(i):
    firstname = names.get_first_name()
    lastname = names.get_last_name()
    salary = random.randint(12000, 2000000)
    start_date = str(random_date(d1,d2))
    uuidx = str(uuid.uuid4())
    insert_sql =  "INSERT INTO [dbo].[Mytable] (id, firstname, lastname,email) VALUES ('TH000000" + str(i) + "','" + firstname + "','" + lastname + "', '" + firstname + lastname + "@xyz.com')"
    return insert_sql

starttime = datetime.utcnow()
print("Starting ingestion: ", starttime.strftime("%Y-%m-%d %H:%M:%S.%f"))
for i in range(no_of_rows):
    insert_row(generate_random_data(i))

endtime = datetime.utcnow()
print("End of ingestion: ", endtime.strftime("%Y-%m-%d %H:%M:%S.%f"))
print("Time taken for " + str(no_of_rows) + " rows: " + str(endtime-starttime))