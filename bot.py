import json
import requests


def handler(event, context):
    data = json.loads(event.get('body'))
    print(data)

    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    resp = requests.post(
        url='https://llm.api.cloud.yandex.net/foundationModels/v1/completion',
        headers={
            "Authorization": "API-KEY AQVNwv6591fyFORy_i5Mf8bTqzhZbllPya7LU8NZ",
            "x-folder-id": "b1ge9cvph0v9mik7cpqv"
        },
        json={
            "modelUri": "gpt://b1ge9cvph0v9mik7cpqv/yandexgpt-lite",
            "completionOptions": {
                "stream": False,
                "temperature": 0.6,
                "maxTokens": "2000"
            },
            "messages": [
                {
                    "role": "system",
                    "text": text
                }
            ]
        }
    )

    answer = resp.json()['result']['alternatives'][0]['message']['text']

    requests.post(
        'https://api.telegram.org/bot7039406207:AAEjffNt2w2GA8Fm6jsjE4iPBJRisrZpE-o/sendMessage',
        json={
            'chat_id': chat_id,
            'text': answer
        }
    )

    return {
        'statusCode': 200,
        'body': 'Hello World!',
    }