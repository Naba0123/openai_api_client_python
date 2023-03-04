import json
import os
import time

import openai
from dotenv import load_dotenv


def log(msg):
    f = open(outfile, 'a')
    f.write(time.strftime('[%Y/%m/%d %H:%M:%S] ') + msg + '\n')
    f.close()


load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

# create result dir
outfile = 'res/' + time.strftime('%Y%m%d%H%M%S.log')
os.makedirs('res/', exist_ok=True)

# initialize messages
messages = [
    {
        'role': 'system',
        'content': '日本語で返答してください。'
    },
]
while True:
    print('> ', end='')
    try:
        ipt = input().strip()
    except EOFError:
        break
    if ipt == '':
        continue
    elif ipt == 'exit':
        break
    messages.append(
        {
            'role': 'user',
            'content': ipt,
        },
    )

    log('You > ' + ipt)

    res = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
    )
    log(json.dumps(res))
    res_msg = res['choices'][0]['message']['content']
    print(res_msg)

    log('AI > ' + res_msg)

print('\n--- Bye. ---\n')
