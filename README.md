# GPT_ClipboardTranslator
事实上这是一个土方法，本意是用来玩生肉galgame时配合MisakaHookFinder使用的。

目前大多数翻译都不大准确，特别是galgame中口语化、不符合语言规范的表达的语句。

而ChatGPT拥有强大的自然语言处理能力，在翻译上强过很多现有的离线字典和在线翻译API，而且ChatGPT还联系上下文，做出更准确的翻译。

# 原理
- 使用[MisakaHookFinder](https://github.com/hanmin0822/MisakaHookFinder)提取galgame内的文本，并将内容实时更新到剪切板；具体使用方法见MisakaHookFinder的介绍，及其相关教程。
- 使用`win32clipboard`读取剪切板内的内容，每0.2秒读取一次，并判断是否与上次读取的内容相同，从而达到实时监控剪切板的效果。
- 由于ChatGPT API貌似是要钱的，而且使用上似乎有各种困难(我没试过，所以不清楚)因此使用了`pyChatGPT`模块；

  我需要再强调一遍，这是个土方法，我不怎么懂电脑、编程之类的，所以也不知道原理；这个其实是我在用[ChatWaifu](https://github.com/cjyaddone/ChatWaifu)的时候想到的，因此甚至干脆就沿用了大佬的`requirements.txt`和环境配置方法。貌似是通过模拟鼠标点击来访问ChatGPT，这个过程需要你提供ChatGPT token或者你的账号及密码(这也意味着你首先需要一个ChatGPT的账号)。
- 使用`win32clipboard`读取到剪切板内最新的内容，然后发送到ChatGPT请求翻译，这个请求具体来说是长下面这个样子的，你可以自己修改，让ChatGPT更准确或者更快速的执行你的指令。
```
while TRUE:
    if i%50 == 0:
        resp = api.send_message("将以下内容翻译成中文(这些待翻译的内容都是相互连续的，句子前有方括号的是相应角色说出来的话，但是其紧挨着的下一到两个待翻译内容有可能也是这个角色说的话，而其他的没有方括号的则是主人公的想法或描述性语句，翻译时请注意前后语义的连贯)："+recent_txt)
    else:
        resp = api.send_message("翻译："+recent_txt)
    i = i+1
```

# 安装环境
