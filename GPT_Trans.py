import win32clipboard
import re
import time
import json
import sys
import os
import logging
from pyChatGPT import ChatGPT

def clipboard_get():
    """获取剪贴板数据"""
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return data

def get_token():
    """获取token"""
    token = input("Copy your token from ChatGPT and press Enter \n")
    return token

logging.getLogger('numba').setLevel(logging.WARNING)

session_token = "<your ChatGPT token>"
#api = ChatGPT(auth_type='google', email='example@gmail.com', password='password')
api = ChatGPT(session_token)
i = 0
while True:
    recent_txt = clipboard_get()
    if i%50 == 0:
        resp = api.send_message("将以下内容翻译成中文(这些待翻译的内容都是相互连续的，句子前有方括号的是相应角色说出来的话，但是其紧挨着的下一到两个待翻译内容有可能也是这个角色说的话，而其他的没有方括号的则是主人公的想法或描述性语句，翻译时请注意前后语义的连贯)："+recent_txt)
    else:
        resp = api.send_message("翻译："+recent_txt)
    answer = resp["message"]
    os.system('cls')
    print(recent_txt,'\n\n',answer)
    while True:
        refresh_txt = clipboard_get()
        if refresh_txt == recent_txt:
            time.sleep(0.2)
        else:
            break
    i=i+1