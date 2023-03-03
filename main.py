import argparse
import json
import os
import time

import openai


def log(msg):
    f = open(outfile, 'a')
    f.write(time.strftime('[%Y/%m/%d %H:%M:%S] ') + msg + '\n')
    f.close()


parser = argparse.ArgumentParser()
parser.add_argument('--apikey')
args = parser.parse_args()
openai.api_key = args.apikey

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
    ipt = input().strip()
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

print('Program Exit. Bye.\n')
