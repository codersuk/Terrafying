import json

def lambda_handler(event, context):
    # TODO implement
    bod= json.loads(event['body'])
    num = bod['number']
    mess = bod['mess']
    x = {"number": num,
         "message": mess,
        "hello": "hello",
        "another":"Another"
    }

    return {
        'statusCode': 200,
        'body': json.dumps(x)
    }
