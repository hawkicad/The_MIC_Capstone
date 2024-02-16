from flask import jsonify

def handleInvalidInput():
    """Return a response for invalid input."""
    return jsonify({"error": "Invalid input"}), 400

def handleDatabaseError(error):
    # Logs the error for debugging purposes
    print(f"Database error: {error}")
    return jsonify({"error": "Database operation failed"}), 500

def handleScraperError(error):
    # Logs the error for debugging purposes
    print(f"Scraper error: {error}")
    return jsonify({"error": "Failed to scrape data"}), 500