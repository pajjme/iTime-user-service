import base64 
import os

# os.urandom() is suitable for cryptographic use
#https://docs.python.org/3/library/os.html#os.urandom
def generate_random_session_key():
    return base64.b64encode(os.urandom(32)).decode("utf-8")
