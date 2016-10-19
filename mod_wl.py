#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Python 2.7.9

import requests
import re

#weblogic 11g
def mod_wl(host,port,usr = 'weblogic',pwd = 'weblogic123'):
	try:
		url = 'http://' + host + ':' + str(port) + '/console/j_security_check'
		payload = {'j_username': usr,'j_password': pwd}
		s = requests.Session()
		r = s.post(url,data = payload)
#		print r.status_code
#		print r.text
		if re.search('domain',r.text):
			print "%s: %s/%s" % (url, usr, pwd)
	except Exception,e:
		print e

if __name__ == '__main__':
	mod_wl('10.223.57.108',7002)


