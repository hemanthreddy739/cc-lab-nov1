import json
print("Function")

def lambda_handler(event, context):
    transactionId = event['queryStringParameters']['transactionId']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']
    
    print('TransactionId = ' + transactionId)
    print('TransactionType = ' + transactionType)
    print('TransactionAmount = ' + transactionAmount)
    
    transactionResponse = {}
    transactionResponse['transactionId'] = transactionId
    transactionResponse['type'] = transactionType
    transactionResponse['amount'] = transactionAmount
    transactionResponse['message'] = 'Hello, welcome from Lambda Function!'
    
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)
    
    return responseObject
    
    
    
    
    #   after -url
    # ?transactionId=14&type=PURCHASE&amount=800

    
    https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbnJPT0ZGUklPTEFrazFoTGUyZ2dhY3EyRVltUXxBQ3Jtc0tuOFB6Skc3ZWxEWVZOamVBaEg0STlXdm9oNExta1JXZWhsdjRpRTZJRVRGLWJXcUZ4V0xhVF9sNjk4aGN3cGtaanFmb3ZzYklnUGpSMHVreE95ajFPQXZrUk9pdGdMd0pWd1ZacEZGUVhJeHJJcTJaaw&q=https%3A%2F%2Fdocs.aws.amazon.com%2FAmazonS3%2Flatest%2Fuserguide%2Fways-to-add-notification-config-to-bucket.html&v=S7SFw8mMMTM
