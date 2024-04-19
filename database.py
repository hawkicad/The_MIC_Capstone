import mysql.connector
from mysql.connector import errorcode

# Removed the user and password as the database is no longer available.
# The database setup document is a good reference for how to create another one that would work the same
config = {
    'host': 'mictestdb.mysql.database.azure.com',
    'user': 'databaseUser',
    'password': 'databasePassword',
    'database': 'mictestdb',
    'client_flags': [mysql.connector.ClientFlag.SSL],
    'ssl_ca': 'DigiCertGlobalRootCA.crt.pem'
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as err:
        print("Failed to connect to database:", err)
        return None

def getDefinitionFromDatabase(word):
    conn = get_db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT definition FROM GlossaryEntry WHERE term = %s;"
            cursor.execute(query, (word.lower(),))  # Assuming 'term' is case-insensitive
            definition = cursor.fetchone()
            cursor.close()
            conn.close()
            if definition:
                return definition[0]
            else:
                return None
        except mysql.connector.Error as err:
            print("Failed to fetch definition:", err)
            return None


def storeGlossaryDataInDatabase(glossary):
    conn = get_db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            insert_query = "INSERT INTO GlossaryEntry (term, definition) VALUES (%s, %s) ON DUPLICATE KEY UPDATE definition = VALUES(definition);"
            for term, definition in glossary.items():
                cursor.execute(insert_query, (term.lower(), definition.lower()))
            conn.commit()
            print("Glossary data stored/updated in database.")
            cursor.close()
        except mysql.connector.Error as err:
            print("Failed to store glossary data:", err)
        finally:
            conn.close()
