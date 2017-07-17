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
	if (event['currentIntent']['slots']['crypto'] != None and len(str(event['currentIntent']['slots']['crypto']))>3 ) :
	    return build_response ("The crypto currency you have selected is invalid. Please try again.")
		
	if (event['currentIntent']['slots']['curr'] != None and len(str(event['currentIntent']['slots']['curr']))>3) :
		return build_response ("Please specify the currency in proper notation, eg. USD or usd")
	
	if (str(event['currentIntent']['slots']['crypto']).lower() == "btc" or str(event['currentIntent']['slots']['crypto']).lower() == "bitcoin") :
		cur_val = "BTC"
	elif (str(event['currentIntent']['slots']['crypto']).lower() == "eth" or str(event['currentIntent']['slots']['crypto']).lower() == "ethereum" or str(event['currentIntent']['slots']['crypto']).lower() == "ether") :
		cur_val = "ETH"
	elif (str(event['currentIntent']['slots']['crypto']).lower() == "ltc" or str(event['currentIntent']['slots']['crypto']).lower() == "litecoin") :
		cur_val = "LTC"
		
	if (event['currentIntent']['slots']['curr'] == None) :
		cur_cur = "USD"
	else :
		cur_cur = str(event['currentIntent']['slots']['curr']).upper()
		
	url = "https://api.coinbase.com/v2/prices/" + cur_val + "-" + cur_cur
	spot_url = url + "/spot"
	buy_url = url + "/buy"
	sell_url = url + "/sell"
	
	try :
		# Add ?currency=x to specify currency
		response = Request(spot_url)
		spotPrice = urlopen(response).read().decode()
		spotPrice = json.loads(spotPrice)
	
		response = Request(buy_url)
		buyPrice = urlopen(response).read().decode()
		buyPrice = json.loads(buyPrice)
	
		response = Request(sell_url)
		sellPrice = urlopen(response).read().decode()
		sellPrice = json.loads(sellPrice)
	
		response = "The spot price of a " + cur_val + " is " + str(spotPrice['data']['amount']) + " " + cur_cur + ".The buy price of a " + cur_val + " is " + str(buyPrice['data']['amount']) + " " + cur_cur + ".The sell price of a " + cur_val + " is " + str(sellPrice['data']['amount']) + " " + cur_cur + "."
	
		return build_response(response)
		
	except :
		return build_response("I'm sorry but coinbase does not appear to support that type of currency.")