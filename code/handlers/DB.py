#!/usr/bin/env python
#-*-coding:utf-8-*-
import logging
import MySQLdb
class DB:
	def __init__(self, ip="", username="", pwd="", database=""):
		try:
			self.conn = MySQLdb.connect(host=ip,user=username,passwd=pwd, charset='utf8')
		except:
			logging.info("can't connect mysql")

		self.curs = self.conn.cursor()
		self.conn.select_db(database)

	def query(self, querystring):
		try:
			self.curs.execute(querystring)
			result = self.curs.fetchall()
		except:
			#logging.info("query failed!")
			result = []
		return result

	def close(self):
		self.conn.close()