#!/usr/bin/env python

import urllib, urllib2, json, datetime
class b99902042:
    def __init__(self, api_key):
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        self.api_key = api_key

    def login(self, account, password, no_data=1):
        self.account = account
	self.password = password
        data = {"username":account, "password":password, "no_data":no_data, "api_key":self.api_key}
        try:
            fp = self.opener.open("http://www.plurk.com/API/Users/login", urllib.urlencode(data))
            return json.loads(fp.read())

        except urllib2.HTTPError, e:
            return json.loads(e.read())

    def relogin(self):
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        return self.login(self.account, self.password)

    def sendData(self, url, data):
        try:
            fp = self.opener.open(url, urllib.urlencode(data))
            return json.loads(fp.read())
        except urllib2.HTTPError, e:
            return json.loads(e.read())

    def getUserID(self, user_id):
        data = {"api_key": self.api_key, "user_id": user_id}
        url = "http://www.plurk.com/API/Profile/getPublicProfile"
        return self.sendData(url,data)


    def getPlurks(self):
	data = {"api_key":self.api_key} 
        try:
		fp = self.opener.open("http://www.plurk.com/API/Timeline/getPlurks", urllib.urlencode(data))
		return json.loads(fp.read())

	except urllib2.HTTPError, e:
		return json.loads(e.read())

    def addResponse(self, plurk_id, content, qualifier="says"):
        # Use http://www.plurk.com/API#/API/Responses/responseAdd
       data = {"api_key":self.api_key,"plurk_id":plurk_id,"content":content,"qualifier":qualifier}
       try:
	       fp = self.opener.open("http://www.plurk.com/API/Responses/responseAdd", urllib.urlencode(data))
	       return json.loads(fp.read())
       except urllib2.HTTPError, e:
	       return json.loads(e.read())
    
    def addPlurk(self, content, qualifier="says"):
	# Use http://www.plurk.com/API#/API/Responses/responseAdd
	data = {"api_key":self.api_key,"content":content,"qualifier":qualifier}
	try:
	       fp = self.opener.open("http://www.plurk.com/API/Timeline/plurkAdd", urllib.urlencode(data))
               return json.loads(fp.read())
        except urllib2.HTTPError, e:
               return json.loads(e.read())

    def openweather(self,string):
       self.string=string
       fp = self.opener.open("http://www.worldweatheronline.com/feed/weather.ashx?q=%s&format=json&num_of_days=2&key=01a892cad9132047101412"%(string))  
       return json.loads(fp.read())

