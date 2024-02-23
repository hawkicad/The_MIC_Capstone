# Mock implementation for local testing

# Temp in-memory database
mockDB = {}

def getDefinitionFromDatabase(word):
    # Simulate fetching a definition from the database
    return mockDB.get(word, None)

def storeGlossaryDataInDatabase(glossary):
    # Simulate storing data in the database
    mockDB.update(glossary)
    print("Mock Database was updated. Current entries: ", len(mockDB))