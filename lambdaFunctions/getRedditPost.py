import json
import urllib
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
    n = 0
    while(n < 10):
        try:
            #Get top post and return it back to user
            req = urllib.urlopen('https://www.reddit.com/r/Crypto_Currency_News/latest/.json?count=0')
            if req.getcode() == 200:
                #req = req.encode('UTF-8')
                req = json.loads(req.read())
                title = str(req['data']['children'][0]['data']['title'])
                url = str(req['data']['children'][0]['data']['url'])
        except:
            return build_response("Unable to get news at this time.")
        
        n += 1
    
    return build_response("The service is currently unavailable. Try again at a later time.")