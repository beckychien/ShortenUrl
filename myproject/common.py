import sqlite3
import socket
from log import MyLog

mylog = MyLog('common')


class Common:
	def fetch_db(sql):
		try:
			con = sqlite3.connect('url.db')
			cursor = con.cursor()
			cursor.execute(sql)
			rows = cursor.fetchall()
			cursor.close()
			con.close()
			return rows

		except Exception as inst:
			mylog.logger.error(sql)
			mylog.logger.error(inst)
			cursor.close()
			con.close()
			raise

	def modify_db(sql):
		try:
			con = sqlite3.connect('url.db')
			cursor = con.cursor()
			cursor.execute(sql)
			con.commit()
			cursor.close()
			con.close()

		except Exception as inst:
			mylog.logger.error(sql)
			mylog.logger.error(inst)
			con.rollback()
			cursor.close()
			con.close()
			raise

	def short_url():
		try:
			digit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

			# get the max id
			rows = Common.fetch_db("SELECT Max(id) FROM URL")
			x = rows[0][0] + 1

			# change id to 62 base to create short url
			s = ""
			while x > 62:
				y = x % 62
				s = digit[y] + s
				x = x // 62
			if x > 0:
				s = digit[x] + s
			return s
		except Exception:
			raise
