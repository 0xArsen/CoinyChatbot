import json
import urllib2
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
    req = urllib2.Request(url='https://www.reddit.com/r/Crypto_Currency_News/new.json?count=0',headers={'User-Agent':'CoinyBot (by /u/pandaxchris'})
    res= urllib2.urlopen(req)   #go through with GET request
    content = res.read()    #Try to read first line
    #Parse into JSON format
    try:
        content = json.loads(content)
        title = str(content['data']['children'][0]['data']['title'])    #Get title of the post
        url = str(content['data']['children'][0]['data']['url'])        #Get link of the news article it points to
    except:
        return build_response("Unable to get news at this time")
    
    return build_response("The service is currently unavailable. Try again at a later time.")
