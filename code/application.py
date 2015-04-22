#!/usr/bin/env python
#-*-coding:utf-8-*-

import os
import tornado.web
import settings
from urls import urls

SettingsDict = dict(
	template_path = os.path.join(os.path.dirname(__file__), "templates"),
	static_path = os.path.join(os.path.dirname(__file__), "static"),
	#cookie_secret = settings.cookie,
	#login_url = settings.login_url, 
	autoescape = None,
	xsrf_cookies = False,
	debug = settings.Debug,
)

application = tornado.web.Application(
	handlers = urls,
	**SettingsDict
)

