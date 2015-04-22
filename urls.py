#!/usr/bin/env python
#-*-coding:utf-8-*-

from handlers.home import HomeHandler
from handlers.home import LineChartSearchHandler, LineChartSearchFuzzHandler, LineChartSearchIPHandler, LineChartQueryResponse


urls = [
(r'/', HomeHandler),
(r'/charts/searchdomain', LineChartSearchHandler),
(r'/charts/searchdomainfuzz', LineChartSearchFuzzHandler),
(r'/charts/searchip', LineChartSearchIPHandler),
(r'/charts/queryresponse', LineChartQueryResponse),
]