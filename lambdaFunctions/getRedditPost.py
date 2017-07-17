import json
import urllib

from urllib.request import Request, urlopen
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
    #return build_response (str(event['currentIntent']['slots']))
    #Get top post and return it back to user'

    reddit = False
    curr = ['bitcoin', 'btc', 'ethereum','eth', 'litecoin', 'ltc']
    if str(event['currentIntent']['slots']['crypto']).lower() in curr:
        req = Request(url='https://www.reddit.com/r/' + event['currentIntent']['slots']['crypto'] + '/top.json?count=2',data={}, headers={'User-Agent':'AWS_chatbot_CoinyBot'})
        reddit = True
    else:
        req = Request(url='https://www.reddit.com/r/Crypto_Currency_News/new.json?count=2', data={}, headers={'User-Agent':'AWS_chatbot_CoinyBot'})
    res = urlopen(req)   #Send GET request
    content = res.read().decode()        #Try to read first line
    #Parse into JSON format
    if not reddit: #Is a news article, user did not specify specific crypto-currency
        try:
            #if res.getcode() == 200:
            content = json.loads(content)
            title = str(content['data']['children'][0]['data']['title'])    #Get title of the post
            url = str(content['data']['children'][0]['data']['url'])        #Get link of the news article it points to
            return build_response(title + ", " + url)
        except:
            return build_response("Unable to get news at this time")
    else:
        try:
            content = json.loads(content)
            title = str(content['data']['children'][0]['data']['title'])
            url = "https://www.reddit.com" + str(content['data']['children'][0]['data']['permalink'])
            return build_response(title + ", " + url)
        except:
            return build_response("Unable to get news at this time")
    
    return build_response("The service is currently unavailable. Try again at a later time.")
