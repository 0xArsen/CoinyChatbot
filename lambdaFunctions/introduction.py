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
    res = ""
    res += "Hello. I am the Coiny bot. My purpose is to help you know about the currrent prices and exchange rates of various bit coins. I hope I can be of help!"
    
    return build_response (res)