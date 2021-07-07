import datetime
import pyodbc
'''   
DriverDetails:ODBC Drive 17 for SQL Server}
ServerName:DESKTOP-N33MAFB
databaseName:RMHS_5MT_rakeDetails
UID:sa
Password:Password@123   
192.168.1.174

# Enable Remote Connections to SQL Server using IP address
https://support.timextender.com/hc/en-us/articles/360042584612-Enable-Remote-Connections-to-SQL-Server-using-IP-address

if ODBC issue is happen then we ened to follow below link.
https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15

'''

# Through this function we can delete data from the SQL table.

def insert_data(Data):

    try:
        print("Try to connect SQL Server for insert data")
        # log.info("Try to connect mssql server")

        # Give sql credentials...
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                              'Server= 192.168.1.147;'
                              # 'Server=DESKTOP-N33MAFB, 1433;'
                              'Database=RMHS_5MT_rakeDetails;'
                              'UID=sa;'
                              'PWD=Password@123;'
                              'MARS_connection=yes;')

        cursor = conn.cursor()
        print("Connection successful")

        if cursor.connection:
            # print("Inside SQL DB")

            # SQl query to insert data.( According to your requirement we need pass the value in list format
            sql = "INSERT INTO Wagon_Entry (DateAndTime, Rake_ID, Wagon_ID) VALUES ('{}','{}','{}');".format(Data[0],Data[1],Data[2])

            # Checking the sql inserting data
            print(" Data Insert query {}".format(sql))

            # Code is execute
            cursor.execute(sql)
            conn.commit()

            # After execute code server will close
            cursor.close()
            conn.close()

            print("Data has been inserted")
            # logger.info("Data has been insert in server-{}-{}".format(Data[0],Data[1]))

        else:

            cursor.close()
            conn.close()

    except Exception as e:
        print("SQL connect failed for insert data", e)
        # log.info("mssql server connection successful")

# Delete Table
def Deletedata():

    try:
        print("Try to connect SQL Server for delete Table info")
        # log.info("Try to connect mssql server")
        # Give sql credentials...
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                              'Server= 192.168.1.147;'
                              # 'Server=DESKTOP-N33MAFB, 1433;'
                              'Database=RMHS_5MT_rakeDetails;'
                              'UID=sa;'
                              'PWD=Password@123;'
                              'MARS_connection=yes;')

        cursor = conn.cursor()
        print("Connection successful for delete table info")

        if cursor.connection:
            # print("Inside SQL DB")

            # SQl query to insert data.( According to your requirement we need pass the value in list format
            sql = "DELETE FROM Wagon_PlacedDetails"
            # sql = "UPDATE Wagon_PlacedDetails SET Message = PLC Received WHERE Message = New Wagon Replace;"

            # Code is execute
            cursor.execute(sql)
            conn.commit()

            # After execute code server will close
            cursor.close()
            conn.close()

            print("Data has been Deleted")
            # logger.info("Data has been insert in server-{}-{}".format(Data[0],Data[1]))

        else:

            cursor.close()
            conn.close()

    except Exception as e:
        print("SQL connect failed for Delete data", e)
        # log.info("mssql server connection successful")


# Checking Function

# k = []
# d = datetime.datetime.now()
# c = "RC252526"
# k.append(d)
# k.append(c)
# print(k)
# # print(k[1])
#
#
#
# insert_data(k)

# if __name__ == '__main__':
#     Deletedata()

