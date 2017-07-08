import boto3
#option_table = boto3.resource('dynamodb').Table('options')
#vote_table = boto3.resource('dynamodb').Table('votes') 

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

def lambda_handler (event, context):

	if 'AccountBalance' == event['currentIntent']['name']:
		#query for balance and store in variable
		return build_response("Account Balance Requested")

	elif 'Addresses' == event['currentIntent']['name']:
		#query for addresses and modify msg using a loop to hold all the addresses
		#msg = " "
		#return build_response(msg)
		return build_response("Addresses Requested")

	elif 'Currency' == event['currentIntent']['name']:
		#query for currency and store in variable
		return build_response("Currency Requested")

	elif 'CurrentPrice' == event['currentIntent']['name']:
		#query for current price and store in variable
		return build_response ("Current Price Requested")

	elif 'SendingMoney' == event['currentIntent']['name']:
		
		return build_response("SendingMoney Requested")

	elif 'Transactions' == event['currentIntent']['name']:
		#query for transactions and modify msg using a loop to hold past x transactions
		#msg = " "
		#return build_response(msg)
		return build_response("Transactions requested")

	elif 'Wallets' == event['currentIntent']['name']:
		#query for wallets and modify msg using a loop to hold past x transactions
		#msg = " "
		#return build_response(msg)
		return build_response("Wallets requested")