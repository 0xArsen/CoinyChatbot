# Coiny - AWSChatbot2017
___

##  What is Coiny?
Coiny is a serverless chatbot built for the AWS 2017 Serverless Chatbot Competition. Any user can text Coiny using their mobile device and they will receive a response to any of their queries about bitcoin or ethereum.
___
## What can Coiny do?
Users can ask price related and reddit news related questions. Information related to price is gathered through the Coinbase API and information about reddit news is gathered through reddit.com
### Sample Questions you can ask:
1. What is the price of bitcoin?
2. What is the price of ethereum?
3. What is the price of BTC in USD?
4. What are the top five posts on r/bitcoin?
5. What is the exchange rate of btc to usd?
___
## How to use Coiny?
The chatbot is deployed on AWS Lex , AWS Lambda and Twilio. This repo contains the AWS Lambda functions and the AWS Lex bot definition file. If you would like to test the bot yourself then you can deploy it on AWS and Twilio.

## Tips for testing

- Use appropriate currency codes when asking for price information (e.g USD, BTC, LTC, ETH)
- Coinbase is only compatible with 3 cryptocurrencies: Bitcoin, Ethereum, Litecoin
- When asking for reddit information you must specify the subreddit as `r/bitcoin`
- DO NOT SPAM THE BOT



# Sample images of bot in action

Spot price request:
![alt text](https://github.com/arsenakishev/AWSChatbot2017/images/spotPrice.png "Spot prices")
