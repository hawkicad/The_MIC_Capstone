import re
from urllib.parse import urlparse

# This function would setup the security configuration. It is a work in progress

"""
def setupSecurity():
    pass
"""


def validateInput(input):
    """Validate input data to prevent injection attacks. Returns True if valid, False otherwise."""
    # Example: Reject input with suspicious characters; customize as needed
    if re.search(r'[<>\"\'%;()&+]', input):
        return False
    return True

def validateURL(url):
    """Validate URL format using urlparse. Returns True if valid, False otherwise."""
    try:
        result = urlparse(url)
        # Basic check: Scheme should be http or https, and netloc should not be empty
        return all([result.scheme in ["http", "https"], result.netloc])
    except Exception:
        return False