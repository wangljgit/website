#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
import logging
import tornado.autoreload
from tornado.options import define, options
from tornado.httpserver import HTTPServer
import settings
from application import application

define("port", default=8888, help="run on the given port", type=int)

def main():
	tornado.options.parse_command_line()
	logging.info("Starting Tornado web server on http:127.0.0.1:%s" % options.port)
	http_server = HTTPServer(application)   
	http_server.listen(options.port) 
	#application.listen(options.port)
	if settings.Debug == True:
		instance = tornado.ioloop.IOLoop.instance()
		tornado.autoreload.start(instance)
		instance.start()
	else:
		tornado.ioloop.IOLoop.instance().start()
	logging.info("Quit the server with CONTROL+C")



if __name__ == '__main__':
	main()