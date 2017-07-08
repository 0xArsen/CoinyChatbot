import boto3

def build_response(message):
	return {
		"dialogAction": {
			"type": "Close",
			"fulfillmentState": "Fulfilled",
			"message": {
				"contentType": "PlainText",
			"content": message
			}
		}
	}



def lambda_handler(event, context):
	if 'Authorize' == event['currentIntent']['name']:
		return build_response("Authorize called")
