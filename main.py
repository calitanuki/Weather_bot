#!/usr/bin/env python
#last update: 2010/11/3 10:21
import time, datetime
from b99902042 import *


def getTime(strTime):
    return datetime.datetime.strptime(strTime, "%a, %d %b %Y %H:%M:%S %Z")

offset = datetime.datetime.now() - datetime.timedelta(0, 24* 3600)
def getValidatePlurks(plurks):
    global offset     
    print "in global"         
    validates = filter(lambda plurk: getTime(plurk["posted"]) > offset and plurk["owner_id"] == 7359258 and getTime(plurk["posted"]) + datetime.timedelta(0,30*60) > datetime.datetime.now() - datetime.timedelta(0,8*3600), plurks)
    offset = max(offset, max( [getTime(plurk["posted"]) for plurk in plurks]))
    print "out global"
    print validates
    return validates


def checkAddResponse(weatherObj, plurk):
	
	print plurk["content"][0:10]
	if plurk["content"][0:10] =="weather of":
		print "in"
		for i in range(12,30):
			if plurk["content"][i]=="?":
	           		string=plurk["content"][11:i-1]
				break
	        print string
                get=weatherObj.openweather(string)["data"]["current_condition"][0]
		print get

		img=get["weatherIconUrl"][0]["value"]
		weatherObj.addResponse(plurk["plurk_id"],img)
		ansa="The cloudcover is %s percent."%(get["cloudcover"])
                ansb="Temperature is %s celsius."%(get["temp_C"])
		ansc="Humidity is %s percent."%(get["humidity"])
		ansd="Wind Speed is %s Kmph."%(get["windspeedKmph"])
		anse="The visibility is %s km."%(get["visibility"])        
		weatherObj.addResponse(plurk["plurk_id"],ansa)
		weatherObj.addResponse(plurk["plurk_id"],ansb)
		weatherObj.addResponse(plurk["plurk_id"],ansc)
		weatherObj.addResponse(plurk["plurk_id"],ansd)
		weatherObj.addResponse(plurk["plurk_id"],anse)

        #timing  = datetime.datetime.now() - datetime.timedelta(0, 24* 3600)
	#while timing > 30*60
    # YOUR TASK: add response!!!!
	print "Your task, find correct plurks and add response"

       # elif getTime(plurk["posted"])


#Read Configure File
f = open("plurk.config", "r")
(account, password, api_key) = [x for x in map(lambda x: x.strip(), f.read().split('\n')) if x != '']


#Create weather Object
weatherObj = b99902042(api_key)
print weatherObj.login(account,password)

string="Taipei"
get1=weatherObj.openweather(string)["data"]["current_condition"][0]
print get1
img1=get1["weatherIconUrl"][0]["value"]
ansa1="The cloudcover is %s percent."%(get1["cloudcover"])
ansb1="Temperature is %s celsius."%(get1["temp_C"])
ansc1="Humidity is %s percent."%(get1["humidity"])
ansd1="Wind Speed is %s Kmph."%(get1["windspeedKmph"])
anse1="The visibility is %s km."%(get1["visibility"])

#weatherObj.addPlurk("Test")

while True:
    try:
        for plurk in getValidatePlurks(weatherObj.getPlurks()["plurks"]):
            checkAddResponse(weatherObj, plurk)
	count=0
        mes="Taipei's weather changed!"
	get2=weatherObj.openweather(string)["data"]["current_condition"][0]
	print get2
	img2=get2["weatherIconUrl"][0]["value"]
	ansa2="The cloudcover is %s percent."%(get2["cloudcover"])
	ansb2="Temperature is %s celsius."%(get2["temp_C"])
	ansc2="Humidity is %s percent."%(get2["humidity"])
	ansd2="Wind Speed is %s Kmph."%(get2["windspeedKmph"])
	anse2="The visibility is %s km."%(get2["visibility"])
	if ansa1!=ansa2:
	        count+=1
	if ansb1!=ansb2:
	        count+=1
	if ansc1!=ansc2:
		count+=1
	if ansd1!=ansd2:
	        count+=1
	if anse1!=anse2:
	        count+=1
	if count!=0:
		#content=mes+ansa2+ansb2+ansc2+ansd2+anse2
		weatherObj.addPlurk("Weather changed! And now the weather of Taipei is %s"%(get2["weatherIconUrl"][0]["value"]))
		weatherObj.addPlurk("Weather changed! Temperature is %s celsius."%(get2["temp_C"]))
		#weatherObj.addResponse(plurk["plurk_id"],ansa2)
		#weatherObj.addResponse(plurk["plurk_id"],ansb2)
		#weatherObj.addResponse(plurk["plurk_id"],ansc2)
		#weatherObj.addResponse(plurk["plurk_id"],ansd2)
		#weatherObj.addResponse(plurk["plurk_id"],anse2)
		ansa1=ansa2
		ansb1=ansb2
		ansc1=ansc2
		ansd1=ansd2
		anse1=anse2
		count=0
	else: 
		print "no change",mes+ansa2+ansb2+ansc2+ansd2+anse2
        	#content=mes+ansa2+ansb2+ansc2+ansd2+anse2
		#weatherObj.addPlurk("Taipei's weather changed! Now the weather is %s"%(get2["weatherIconUrl"][0]["value"]))
		#weatherObj.addPlurk("Taipei's weather changed!Temperature is %s celsius."%(get2["temp_C"]))
    except  KeyError, e:
        #handle the login timeout 
       print "key"
       weatherObj.relogin()

    except Exception, e:
       print "key2"	    
       print e
   
    time.sleep(10)
