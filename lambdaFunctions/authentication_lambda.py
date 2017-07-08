import json

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['code'])
    #print("value2 = " + event['key2'])
    #print("value3 = " + event['key3'])
    phrase = "This is the authentication code: " + event['code']
    return phrase # Echo back the first key value
    #raise Exception('Something went wrong')
