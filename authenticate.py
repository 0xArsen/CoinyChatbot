import boto3
import json
from random import randint
import os
import urllib
from urllib.parse import urlencode
from urllib.request import Request, urlopen

coiny = boto3.resource('dynamodb').Table('Coiny')
ses = boto3.client('ses')

email_from = 'ql523@nyu.edu'
#coinbase_API_url = "https://api.coinbase.com/v2/"

grant_type = 'authorization_code'
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
redirect_uri = os.environ.get("REDIRECT_URI")

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

	'''
	Get access token and refresh token from coinbase
	'''
	coinbase_POST_url = "https://api.coinbase.com/oauth/token"
	post_fields = {'grant_type' : grant_type, 'code' : event['code'], 'client_id' : client_id, 'client_secret' : client_secret}
	#print('grant_type' + grant_type + 'code' + event['code'] + 'client_id' + client_id + 'client_secret' + client_secret + 'redirect_uri' + redirect_uri)
	data = urlencode(post_fields)
	data += '&redirect_uri=' + redirect_uri
	data = json.dumps(data)
	req = Request(coinbase_POST_url, data.encode('ascii'))
	json.dumps(cls=req)
	return req
	json1 = urlopen(req).read().decode()
	json1 = json.loads(json1)

	access_token = json1['access_token']
	refre_token = json1['refresh_token']

	'''
	Get email and name of the user
	'''
	coinbase_API_url = "https://api.coinbase.com/v2/user/"
	post_fields2 = {'Authorization' : 'Bearer {}'.format(access_token)}
	information = Request(coinbase_POST_url, urlencode(post_fields).encode())
	json2 = urlopen(information).read().decode()
	json2 = json.loads(json2)

	email = json2['username']
	name = json2['name']
	user_ID = json2['id']

	'''
	Generate Temporary user id for storage in dynamodb
	'''
	randNum = randint(1000, 9999)

	'''
	Ensure that the temporary user id is unique
	'''
	while (True):
		try:
			item = coiny.get_item(
				Key = {
					'Phone_num': str(randNum)
				})
			randNum = randint(1000, 9999)
		except:
			break


	'''
	Send email to user for Two Factor authentication with unique id attached
	'''
	response = ses.send_email(
		Source = email_from,
		Destination={
			'ToAddresses': [
				email_from,
			],
			'CcAddresses': [

			]
		},
		Message={
			'Subject': {
				'Data': 'Coiny-Coinbase Verification Email'
			},
			'Body': {
				'Text': {
					'Data': str(randNum)
				}
			}
		}
	)

	'''
	Store user using temporary id
	'''
	resp = coiny.put_item(
		Item = {
			'Phone_num': str(randNum),
			'Email': email,
			'Name': name,
			'access_token': access_token,
			'refre_token': refre_token,
			'user_ID' : user_ID
		}
	)

	return build_response("E-mail token has been sent. Please validate by sending us this token.")
