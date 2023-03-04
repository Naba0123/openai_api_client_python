import json
import math
import os
import sys
import time
import readline

import openai
from dotenv import load_dotenv

from color import Color


def log(msg):
    f = open(outfile, 'a')
    f.write(time.strftime('[%Y/%m/%d %H:%M:%S.%f] ') + msg + '\n')
    f.close()


def out(msg, cl=Color.COLOR_DEFAULT, end='\n'):
    print(f'{cl}{msg}{Color.RESET}', end=end)
    sys.stdout.flush()


_ = readline  # unused but want to import
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

# main loop
while True:
    out('--- You ---', Color.CYAN)
    try:
        ipt = input().strip()
    except (EOFError, KeyboardInterrupt):
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

    out('AI thinking...', Color.MAGENTA, end='')

    start_time = time.perf_counter()
    res = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
    )
    end_time = time.perf_counter()

    log(json.dumps(res))
    res_msg = res['choices'][0]['message']['content']

    print("\033[2K\033[G", end='')
    out('--- AI --- ({}ms)'.format(math.ceil((end_time - start_time) * 1000)), Color.YELLOW)
    out(res_msg, Color.YELLOW)
    log('AI > ' + res_msg)

    messages.append(
        {
            'role': 'assistant',
            'content': res_msg,
        },
    )

print('\nBye.')
