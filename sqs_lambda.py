import json

def lambda_handler(event, context):
    print(event)
    for record in event.get('Records'):
        body = json.loads(record.get('body'))
        id_person = body.get('id')
        name = body.get('name')
        print(f'Name: {name}', f'ID:{id_person}')
        return {
        'statusCode': 200,
       
    }
