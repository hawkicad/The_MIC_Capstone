from flask import Flask, request, jsonify
import database
import scraper
import security
import error_handling

# These endpoints are drafts of what will be used once we have merged the current drafted code
# The testing and revisions will be done next week

def initializeAPIServer(app):
    @app.route('/definition/<word>', methods=['GET'])
    def getDefinitionEndpoint(word):
        word = word.lower()
        if not security.validateInput(word):
            return error_handling.handleInvalidInput()
        try:
            definition = database.getDefinitionFromDatabase(word)
            if definition:
                return jsonify(definition=definition)
            else:
                return jsonify(error="Word not found"), 404
        except Exception as e:
            return error_handling.handleDatabaseError(e)

    @app.route('/update', methods=['POST'])
    def updateGlossaryDatabase():
        url = "https://lpi.oregonstate.edu/mic/glossary"
        if not security.validateURL(url):
            return error_handling.handleInvalidInput()
        try:
            glossaryData = scraper.scrapeGlossary(url)
            database.storeGlossaryDataInDatabase(glossaryData)
            return jsonify(message="Scraping and Storage Successful")
        except Exception as e:
            return error_handling.handleScraperError(e)