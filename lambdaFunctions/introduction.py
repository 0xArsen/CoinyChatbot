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
    res += "Hello. I am the Coiny bot. My purpose is to help you gather information about cryptocurrencies. I hope to be of great service!"

    return build_response (res)
