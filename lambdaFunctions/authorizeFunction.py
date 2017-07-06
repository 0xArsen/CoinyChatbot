import boto3


def lambda_handler(event, context):
	if 'Authorize' == event['currentIntent']['name']:
		print("Authorize called")
