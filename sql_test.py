import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
    'host':'mictestdb.mysql.database.azure.com',
    'user':'c_hawk7397',
    'password':'m1(|<3yM0i_i53',
    'database':'mictestdb',
    'client_flags': [mysql.connector.ClientFlag.SSL],
    'ssl_ca': 'DigiCertGlobalRootCA.crt.pem'
}

# Construct connection string
try:
    conn = mysql.connector.connect(**config)
    print("Connection established")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = conn.cursor()

    # Read data
    cursor.execute("SELECT * FROM GlossaryEntry;")
    rows = cursor.fetchall()
    print("Read",cursor.rowcount,"row(s) of data.")

    # Print all rows
    for row in rows:
  	    print("Data row = (%s, %s)" %(str(row[0]), str(row[1])))
           
    # Cleanup
    conn.commit()
    cursor.close()
    conn.close()
    print("Done.")