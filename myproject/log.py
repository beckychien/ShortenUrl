import logging
import logging.handlers


class MyLog(object):
	def __init__(self, appname):
		self.logger = logging.getLogger(appname)
		if not self.logger.handlers:
			filename = 'log/' + appname + '.log'
			# 設定日誌格式
			format = '%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(lineno)d : %(message)s'
			formatter = logging.Formatter(format)

			# 日誌輸出到畫面
			sh = logging.StreamHandler()
			sh.setFormatter(formatter)
			# 設置日誌等级
			self.logger.setLevel(logging.INFO)

			# 保存日誌到文件(200K換新檔案，最多保存三個檔案)
			fh = logging.handlers.RotatingFileHandler(
				filename=filename, maxBytes=200000, backupCount=3)
			fh.suffix = "%Y-%m-%d.log"
			fh.setFormatter(formatter)
			# 設置日誌等级
			fh.setLevel(logging.INFO)

			self.logger.addHandler(fh)
			self.logger.addHandler(sh)

	def debug(self, msg):
		self.logger.debug(msg)

	def info(self, msg):
		self.logger.info(msg)

	def warning(self, msg):
		self.logger.warning(msg)

	def error(self, msg):
		self.logger.error(msg)

	def critical(self, msg):
		self.logger.critical(msg)

	def log(self, level, msg):
		self.logger.log(level, msg)

	def setLevel(self, level):
		self.logger.setLevel(level)

	def disable(self):
		logging.disable(50)
