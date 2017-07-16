import boto3
import json 
import urllib
from urllib.parse import urlencode
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
	
	cur_val = ""
	cur_cur = ""
	
	if (event['currentIntent']['slots']['crypto'] == None) :
		return build_response ("Please specify the cryptocurrency in proper notation, eg. BTC or btc")
	
	if (event['currentIntent']['slots']['curr'] != None and len(str(event['currentIntent']['slots']['curr']))>3) :
		return build_response ("Please specify the currency in proper notation, eg. USD or usd")
		
	if (str(event['currentIntent']['slots']['crypto']).lower() == "btc" or str(event['currentIntent']['slots']['crypto']).lower() == "bitcoin") :
		cur_val = "BTC"
	elif (str(event['currentIntent']['slots']['crypto']).lower() == "eth" or str(event['currentIntent']['slots']['crypto']).lower() == "ethereum" or str(event['currentIntent']['slots']['crypto']).lower() == "ether") :
		cur_val = "ETH"
	elif (str(event['currentIntent']['slots']['crypto']).lower() == "ltc" or str(event['currentIntent']['slots']['crypto']).lower() == "litecoin") :
		cur_val = "LTC"
		
	cur_cur = str(event['currentIntent']['slots']['curr']).upper()
	
	url = "https://api.coinbase.com/v2/exchange-rates?currency=" + cur_val
	
	response = Request(url)
	built_res = urlopen(response).read().decode()
	built_res = json.loads(built_res)
	
	if cur_cur in built_res['data']['rates'] :
		val = built_res['data']['rates'][cur_cur]
		return build_response("The exchange rate for " + cur_val + " in " + cur_cur + " is " + val + ".")
	else :
		return build_response("Coinbase does not support the specified currency")
		