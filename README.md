# Coiny - AWSChatbot2017
___

##  What is Coiny?
Coiny is a serverless chatbot built for the AWS 2017 Serverless Chatbot Competition. Any user can text Coiny using their mobile device and they will receive a response to any of their queries about bitcoin or ethereum.
___
## What can Coiny do?
Users can ask price related and reddit post related questions. Information related to price is gathered through the Coinbase API and information about reddit posts is gathered through reddit.com
### Sample phrases you can send:
1. What is the price of bitcoin?
2. What is the price of ethereum?
3. give me news about Litecoin
3. What is the price of BTC in USD?
4. What's going on with ethereum.
5. What is the exchange rate of btc to usd?
___
## How to use Coiny?
The chatbot is deployed on AWS Lex , AWS Lambda and Twilio. This repo contains the AWS Lambda functions and the AWS Lex bot definition file. If you would like to test the bot yourself then you can deploy it on AWS and Twilio.

Since the bot is deployed on Twilio and the account we have is in trial mode then we will need to verify any phone number thats wishes to send a text to Coiny for testing purposes. If you would like to have your number verified then please email Arsen at `arsenakishev@gmail.com`.

## Tips for testing

- Use appropriate currency codes when asking for price information (e.g USD, BTC, LTC, ETH)
- Coinbase is only compatible with 3 cryptocurrencies: Bitcoin, Ethereum, Litecoin
- When asking for reddit information you must specify the cryptocurrency
- DO NOT SPAM THE BOT
