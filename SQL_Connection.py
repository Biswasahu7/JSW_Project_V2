import datetime
import pyodbc
# print(pyodbc.drivers())
# from mysql.connector
# import mysql.connector
# ODBC Driver 17 for SQL Server
# ODBC Driver 17 for SQL Server
try:
    print("Try to Connect")
    # log.info("Try to connect mssql server")
    # conn = pyodbc.connect('DRIVER={ODBC Drive  r 17 for SQL Server};Server=DESKTOP-N33MAFB;Database=RMHS_5MT_rakeDetails;UID=sa;PWD=Password@123;MARS_connection=yes')
    #conn = pymssql.connect(server='172.21.25.164', user='sa', password='admin@123', database='cvml')
    # cursor = conn.cursor()
    # cursor.execute('''CREATE TABLE TWarning (CameraName nvarchar(50),WarningName nvarchar(50),Time datetime, CameraIP nvarchar(50), Objectname nvarchar(50) ''')
    # print("Table created")
    # conn.commit()
    # for row in cursor.columns(table='tblWarning'):
    #
    #       print(row.column_name)
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'Server= 192.168.1.147;'
                          # 'Server=DESKTOP-N33MAFB, 1433;'
                          'Database=RMHS_5MT_rakeDetails;'
                          'UID=sa;'
                          'PWD=Password@123;'
                          'MARS_connection=yes;')

    cursor = conn.cursor()
    print("Connection successful")

    query = "SELECT Message FROM Wagon_PlacedDetails;"
    cursor.execute(query)
    myresult = cursor.fetchall()
    value = []

    for i in myresult:
        # print(type(i))
        # print(i)
        value.append(i)
    # print(value[0][0])

    if value[0][0] == "New Wagon Placed":
        print("Matching condition")

    # USing mysql connector
    # mydb = mysql.connector.connect(user='sa', passwd='Password@123',
    #                                  host='192.168.1.147')
    #                                  # database='RMHS_5MT_rakeDetails')
    #
    # mycursor = mydb.cursor()
    # mycursor.execute()
    # for i in mycursor:
    #     print(i)

    # cursor.close()
    # conn.close()
    # log.info("mssql server connection successful")

except Exception as e:
    print("connection failed", e)
    # log.error("mssql server connection failed {}".format(e))