import httplib, urllib
import os
import yaml


def validate(text,port_no):
	params = urllib.urlencode({'text': text, 'language': 'en-US'})
	headers = {"Content-type": "x-www-form-urlencoded", "Accept": "xml"}
	conn = httplib.HTTPConnection("localhost",port_no)
	conn.request("POST","/v2/check",params,headers)
	response = conn.getresponse()
	data = response.read()
	data = yaml.load(data)

	loc = []
	rule = []
	msg = []
	replacements = []

	for i in range(len(data["matches"])):
		loc.append((data["matches"][i]['length'],data["matches"][i]['offset']))
		rule.append(data["matches"][i]['rule']['id'])
		msg.append(data["matches"][i]['shortMessage'])
		replacements.append(data["matches"][i]['replacements'])
	
	return {'Location':loc,'Rule':rule,'Message':msg,'Replacements':replacements}