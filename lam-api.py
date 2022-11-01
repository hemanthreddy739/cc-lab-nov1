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
