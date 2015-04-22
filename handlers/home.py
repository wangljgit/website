#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@Author: Wanglj
Created on 2015-4-19
Last modified
网站主页
'''
import logging
import json
import tornado.web
import torndb
import time
from DB import DB
# class DB:
# 	def __init__(self):
# 		self.db = torndb.Connection("172.26.253.30", "test", user="root", password="nislab")

class GetTime:
	def __init__(self):
		self.monDay = [31, 28, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31]
	def getHour(self, tm_year, tm_mon, tm_mday,tm_hour):
		#判断是否刚过0点
		if tm_hour == 0:
			#判断是否为每个月第一天
			if tm_mday == 1:
				#判断是否为1月
				if tm_mon == 1:
					#是1月1号0点，则分析上一年的12月31日23点一个小时的数据包
					tm_hour = 23
					tm_mday = 31
					tm_mon = 12
					tm_year = tm_year - 1
				else:
					tm_mon = tm_mon - 1
					tm_hour = 23
					tm_mday = self.monDay[tm_mon]
					if tm_mon == 2:
						#判断闰年条件, 满足模400为0, 或者模4为0但模100不为0
						if (tm_year % 400 == 0) or (tm_year % 4 ==0 and tm_year % 100 != 0):
							tm_mday = tm_mday + 1
			else:
				tm_hour = 23
				tm_mday = tm_mday - 1
		else:
			tm_hour = tm_hour - 1
		return tm_year, tm_mon, tm_mday, tm_hour

	def getNowTime(self):
		timestamp = time.time()
		localtime = time.localtime(timestamp)
		tm_year = localtime[0]
		tm_mon = localtime[1]
		tm_mday = localtime[2]
		tm_hour = localtime[3]
		return tm_year, tm_mon, tm_mday, tm_hour

class HomeHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")

def getTime(domainname, fuzz=0, table="1querydomain", date="20150422"):
	gettime = GetTime()
	db = DB()
	# timestamp = time.time()
	# localtime = time.localtime(timestamp)
	queryResult = []
	querystring = ""

	tm_year, tm_mon, tm_mday, tm_hour = gettime.getNowTime()
	today = "%d%02d%02d" % (tm_year, tm_mon, tm_mday)
	if today != date:
		tm_hour = 24
	for i in range(tm_hour):
		#tm_year, tm_mon, tm_mday, tm_hour = gettime.getHour(tm_year, tm_mon, tm_mday, tm_hour)
		#hourstring = 
		timestring = "select number from " + date + ("%02d" % ( i))
		if fuzz:
			#querystring = "select number from %d%02d%02d%02d1querydomain where name like '%%%s'" % (tm_year, tm_mon, tm_mday, i, domainname)
			tempstring = " where name like '%%%s'" % (domainname)
			querystring = timestring + table + tempstring
		else:
			tempstring = " where name='%s'" % (domainname)
			querystring = timestring + table + tempstring
		try:
			results = db.query(querystring)
			#logging.info("query result")
			if results:
				#logging.info("query in result fuzz is %d", fuzz)
				if fuzz:
					#logging.info("in fuzz")
					number = 0
					for result in results:
						number = number + result[0]
					queryResult.append(number)
					#logging.info("fuzz number is %d", number)
				else:
					#logging.info("time number is %d", results[0][0])
					queryResult.append(results[0][0])
			else:
				#logging.info("results is empty ")
				queryResult.append(0)
		except Exception, e:
			print str(e)
			logging.info("query number failed!")
			queryResult.append(0)
	#lastResult =  queryResult[::-1]
	db.close()
	return queryResult

class LineChartSearchHandler(tornado.web.RequestHandler):
	def get(self):
		domainname = self.get_argument('domainname', 'nodomain')
		date = self.get_argument("date")
		#result = self.db.db.query("select * from 20150420181querydomain where name=%s;", domainname)
		result = getTime(domainname, 0, "1querydomain", date)
		if result:
			self.write(json.dumps(result))
			self.finish()
		#self.write("www.baidu.com")
			
		logging.info('result is %s' % result)

class LineChartSearchFuzzHandler(tornado.web.RequestHandler):
	# def getTime(self, domainname):
	# 	gettime = GetTime()
	# 	db = DB()
	# 	timestamp = time.time()
	# 	localtime = time.localtime(timestamp)
	# 	queryResult = []

	# 	tm_year = localtime[0]
	# 	tm_mon = localtime[1]
	# 	tm_mday = localtime[2]
	# 	tm_hour = localtime[3]
	# 	#logging.info("now time is %d" % tm_hour)
	# 	for i in range(tm_hour):
	# 		#tm_year, tm_mon, tm_mday, tm_hour = gettime.getHour(tm_year, tm_mon, tm_mday, tm_hour)
	# 		querystring = "select number from %d%02d%02d%02d1querydomain where name='%s'" % (tm_year, tm_mon, tm_mday, i, domainname)
	# 		try:
	# 			result = db.db.query(querystring)
	# 			if result:
	# 				queryResult.append(result[0]['number'])
	# 			else:
	# 				queryResult.append(0)
	# 		except Exception, e:
	# 			queryResult.append(0)
	# 	#lastResult =  queryResult[::-1]
	# 	return queryResult

		
	def get(self):
		domainname = self.get_argument('domainname', 'nodomain')
		date = self.get_argument('date')
		#result = self.db.db.query("select * from 20150420181querydomain where name=%s;", domainname)
		result = getTime(domainname, 1, "1querydomain", date)
		if result:
			self.write(json.dumps(result))
			self.finish()
		#self.write("www.baidu.com")
			
		logging.info('result is  %s' % result)

class LineChartSearchIPHandler(tornado.web.RequestHandler):
	def get(self):
		queryip = self.get_argument('queryip', '127.0.0.1')
		iptype = self.get_argument('iptype', 'src')
		date = self.get_argument("date")
		if iptype=="src":
			table = "1srcip"
		else :
			table = "1dstip"
		#result = self.db.db.query("select * from 20150420181querydomain where name=%s;", domainname)
		result = getTime(queryip, 0, table, date)
		if result:
			self.write(json.dumps(result))
			self.finish()
		#self.write("www.baidu.com")
			
		logging.info('result is %s' % result)

def getQueryResponse(date):
	db = DB()
	gettime = GetTime()
	queryResult = []
	responseResult = []
	querystring = ""
	tm_year, tm_mon, tm_mday, tm_hour = gettime.getNowTime()
	today = "%d%02d%02d" % (tm_year, tm_mon, tm_mday)
	# if today == date:
	# 	querystring = "select number from %d%02d%02d%02d1querydomain;" % (tm_year, tm_mon, tm_mday, i)
	# 	responsestring = "select number from %d%02d%02d%02d2querydomain;" % (tm_year, tm_mon, tm_mday, i)
	# else:
	# 	querystring = "select number from " + date + "1querydomain;"
	# 	responsestring = "select number from " + date + "2querydomain;"
	# 	tm_hour = 24
	if today != date:
		tm_hour = 24

	for i in range(tm_hour):
		#tm_year, tm_mon, tm_mday, tm_hour = gettime.getHour(tm_year, tm_mon, tm_mday, tm_hour)
		table = "%02d1querydomain;" % i
		querystring = "select number from " + date + table
		table = "%02d2querydomain;" % i
	 	responsestring = "select number from " + date + table
		try:
			results = db.query(querystring)
			if results:
				number = 0
				for result in results:
					number = number + result[0]
				queryResult.append(number)
			else:
				queryResult.append(0)
		except Exception, e:
			print str(e)
			logging.info("query number failed!")
			queryResult.append(0)

		try:
			results = db.query(responsestring)
			if results:
				number = 0
				for result in results:
					number = number + result[0]
				responseResult.append(number)
			else:
				responseResult.append(0)
		except Exception, e:
			print str(e)
			logging.info("response number failed!")
			responseResult.append(0)
	#lastResult =  queryResult[::-1]
	db.close()
	return queryResult, responseResult

class LineChartQueryResponse(tornado.web.RequestHandler):
	def get(self):
		result = []
		date = self.get_argument("date")
		queryresult, responseresult = getQueryResponse(date)
		result.append(queryresult)
		result.append(responseresult)
		self.write(json.dumps(result))
		self.finish()
		#self.write("www.baidu.com")
		logging.info('result is %s' % result)
