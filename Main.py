from flask import Flask
import api

# Commented out, but included as they will later be necessary
#import database
import security

app = Flask(__name__)

def startServer():
    #database.setupDatabase()
    api.initializeAPIServer(app)

if __name__ == '__main__':
    startServer()
    app.run(debug=True)