import json
<<<<<<< HEAD
import urllib

from urllib.request import Request, urlopen
=======
import urllib2
>>>>>>> 3e13df648ff21bb7a5f3dbf37061946cac44d7b4
def build_response(message):
	return {
		"dialogAction" : {
			"type": "Close",
			"fulfillmentState": "Fulfilled",
			"message": {
				"contentType": "PlainText",
				"content": message
			}
		}
	}

def lambda_handler(event, context):
    #Get top post and return it back to user'
<<<<<<< HEAD
    req = Request(url='https://www.reddit.com/r/Crypto_Currency_News/new.json?count=2', data={}, headers={'User-Agent':'AWS_chatbot_CoinyBot'})
    res = urlopen(req)   #Send GET request
    content = res.read().decode()        #Try to read first line
    #Parse into JSON format
    try:
        #if res.getcode() == 200:
        content = json.loads(content)
        title = str(content['data']['children'][0]['data']['title'])    #Get title of the post
        url = str(content['data']['children'][0]['data']['url'])        #Get link of the news article it points to
        return build_response(title + ", " + url)
    except:
        return build_response("Unable to get news at this time")

=======
    req = urllib2.Request(url='https://www.reddit.com/r/Crypto_Currency_News/new.json?count=0',headers={'User-Agent':'CoinyBot'})
    res= urllib2.urlopen(req)   #go through with GET request
    content = res.read()    #Try to read first line
    #Parse into JSON format
    try:
        content = json.loads(content)
        title = str(content['data']['children'][0]['data']['title'])    #Get title of the post
        url = str(content['data']['children'][0]['data']['url'])        #Get link of the news article it points to
    except:
        return build_response("Unable to get news at this time")
    
>>>>>>> 3e13df648ff21bb7a5f3dbf37061946cac44d7b4
    return build_response("The service is currently unavailable. Try again at a later time.")
