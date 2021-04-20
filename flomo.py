#!/bin/env python
# -*- coding: UTF-8 -*-
import os, sys, re, json
import requests
import subprocess


def flomo_post(flomoapi, headers, content):
    print(flomoapi)

    r = requests.post(flomoapi, headers=headers, json={'content':f'{content}'})

    print("----------------")
    print(content)
    print("----------------")
    print(r)
    # print(r.__dict__)
    # print(r._content)
    # print(r.content)
    print(r.text)
    ret = json.loads(r.text)
    print(ret)
    if r.status_code == 200 and ret['code'] == 0:
        print ('MEMO 创建成功')
    else:
        print ('MEMO 创建失败。内容宝贵，请注意保存！')

headers = {'Content-Type': 'application/json;charset=UTF-8'}
flomoapi = os.getenv('FLOMOAPI')
flomoeditor = os.getenv('FLOMOEDITOR')

if not flomoapi:
    print("请先创建 FLOMOAPI 环境变量")
    exit()

content=''

if len(sys.argv) <= 1:
    if not flomoeditor:
        print("请先创建 FLOMOEDITOR 环境变量")
        exit()

    print('hint: Waiting for your editor to close the file... ')
    print('提示: 正在等待编辑器关闭文件... ')

    sys.stdout.flush()

    # c = subprocess.run(["subl", "-w", "FLOMO_EDITMSG"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # print(c.stdout.decode('utf-8'))

    stream = os.popen(flomoeditor + ' ' + "FLOMO_EDITMSG")
    output = stream.read()

    with open('FLOMO_EDITMSG', "r", encoding='utf-8') as f:
        content = f.read()

    # print("姿势不对。用法：flomo.py '文本...'")
    # exit()
else:

    for argv in sys.argv[1:]:
        content +=  argv + '\n'

    if '#' not in content:
        content = '#待整理\n' + content

flomo_post(flomoapi, headers, content)

