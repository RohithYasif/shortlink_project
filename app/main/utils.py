# app/main/utils.py
import re
from random import choices
import string

# URL validation
def is_valid_url(url):
    url_regex = re.compile(r"^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$")
    return re.match(url_regex, url) is not None

# Generate a unique short code
def generate_short_code(length=6):
    return ''.join(choices(string.ascii_letters + string.digits, k=length))
