from flask import Flask, request, redirect
from urllib.parse import urlparse
from common import Common
from log import MyLog
import requests
import sqlite3
import traceback

app = Flask(__name__)
mylog = MyLog('app')


@app.route("/ShortUrl", methods=['GET'])
def short_request():
	"""
	use 62 base to shorten original URL and insert original URL, short URL to DB.
	:return:
	short URL
	"""
	try:
		# change ip parameter to the real server ip
		ip = "127.0.0.1"
		url_prefix = "http://" + ip + "/"
		longURL = request.values.get('url')
		parsed = urlparse(longURL)
		if parsed.scheme:
			shortURL = Common.short_url()
			Common.modify_db("INSERT INTO URL (longURL,shortURL) VALUES('{}','{}')".format(longURL, shortURL))
			return url_prefix + shortURL
		else:
			return "The url is unavailable."
	except Exception as inst:
		mylog.logger.error(inst)
		mylog.logger.error(traceback.format_exc())
		return "Exception happened"


@app.route("/<shortURL>", methods=['GET'])
def redirect_to_url(shortURL):
	"""
    use short url to get original url from db, then redirect to original url.
    """
	try:
		url = Common.fetch_db("SELECT longURL FROM URL WHERE shortURL = '{}' ".format(shortURL))
		if url is None or not url[0][0]:
			return "Not found original URL."
		return redirect(url[0][0])

	except Exception as inst:
		mylog.logger.error(inst)
		mylog.logger.error(traceback.format_exc())
		return "Exception happened"


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=5000)
