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
    res += "Sample phrases you can ask: |what is the price of bitcoin| |give me news about ethereum|"

    return build_response (res)
