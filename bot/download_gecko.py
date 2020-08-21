import os
import zipfile
import shutil
import requests

def baixardriver():
	if os.path.isfile('/Program Files/Instagram/geckodriver.exe') == False:

			r = requests.get('https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win32.zip')

			with open('/Program Files/Instagram/gecko.zip', 'wb') as f:
				f.write(r.content)

			shutil.unpack_archive('/Program Files/Instagram/gecko.zip', '/Program Files/Instagram/')

