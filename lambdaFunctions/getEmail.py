from coinbase.wallet.client import OAuthClient
import urllib
import urllib2
import json
import requests
CLIENT_ID = 'c4c8821329affe9e4eefe6c134c889a0a1047b0a2b8a04b2fd8c3b3d853cb73f'
CLIENT_SECRET = 'b486e8e52d5f895dfe0246933b23d6eb25d7684de83f58610728a12ce0607dac'
access_token = "671cf6d33638889d6840304e4d3bc2ed7078cd6877749b47a042c0868ea82d74"
refresh_token = "97926c115b174a71a6aa48b444a9f908dd585ef87c8e2e319376b09751789ae3"
code= '6cf0e8b7457610ecb1c5a3c12985e1f6580dcef81b96f304416ce989f740608b'
client = OAuthClient(access_token, refresh_token)

def main():
    redirect_uri = 'https://q8bcq3luah.execute-api.us-east-1.amazonaws.com/004RedirectStage'
    url = "https://api.coinbase.com/oauth/token/"
    payload = {'grant_type' : 'authorization_code',
        'code' : code,
        'client_id' : CLIENT_ID,
        'client_secret' : CLIENT_SECRET,
        'redirect_uri' : redirect_uri
        }

    new_payload = "grant_type=authorization_code&code=" +  code + "&client_id=" + CLIENT_ID + "&client_secret=" +  CLIENT_SECRET + "&redirect_uri=" + redirect_uri
    payload_json = json.dumps(payload)
    contentType = 'application/x-www-form-urlencoded; charset=UTF-8'
    headers = {}
    headers['Content-Type'] = contentType
    data = urllib.urlencode(payload)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    result = response.read()
    print result
    


'''
    req = requests.post("https://api.coinbase.com/oauth/token",  data=json.dumps(payload))
    print (req.headers.get('content-type'))
    print req.text
'''


#   price = client.get_buy_price(currency_pair = 'BTC-USD')
#   print price
    #user = client.get_current_user()
    #user_as_json_string = json.dumps(user)
    #print user_as_json_string
if __name__ == "__main__":
    main()
