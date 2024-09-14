import json
import requests


def handler(event, context):
    data = json.loads(event.get('body'))
    print(data)

    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    resp = requests.post(
        url='https://llm.api.cloud.yandex.net/foundationModels/v1/completion', #you can have the different one
        headers={
            "Authorization": "API-KEY {YAGPT_API_KEY}",
            "x-folder-id": "{YAGPT_FOLDER_ID}"
        },
        json={
            "modelUri": "gpt://{YAGPT_FOLDER_ID}/yandexgpt-{MODEL_TYPE}",
            "completionOptions": {
                "stream": False,
                "temperature": {TEMPERATURE},
                "maxTokens": "{MAX_TOKENS}"
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
        'https://api.telegram.org/bot{BOT_TOKEN/sendMessage',
        json={
            'chat_id': chat_id,
            'text': answer
        }
    )

    return {
        'statusCode': 200,
        'body': 'Hello World!',
    }
