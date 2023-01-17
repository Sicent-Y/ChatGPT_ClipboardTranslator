# GPT_ClipboardTranslator
事实上这是一个土方法，本意是用来玩生肉galgame时配合MisakaHookFinder使用的。

目前大多数翻译都不大准确，特别是galgame中口语化、不符合语言规范的表达的语句。

而ChatGPT拥有强大的自然语言处理能力，在翻译上强过很多现有的离线字典和在线翻译API，而且ChatGPT还联系上下文，做出更准确的翻译。

# 原理
- 使用[MisakaHookFinder](https://github.com/hanmin0822/MisakaHookFinder)提取galgame内的文本，并将内容实时更新到剪切板；具体使用方法见MisakaHookFinder的介绍，及其相关教程。
- 使用`win32clipboard`读取剪切板内的内容，每0.2秒读取一次，并判断是否与上次读取的内容相同，从而达到实时监控剪切板的效果。
- 由于ChatGPT API貌似是要钱的，而且使用上似乎有各种困难(我没试过，所以不清楚)因此使用了`pyChatGPT`模块；

  我需要再强调一遍，这是个土方法，我不怎么懂电脑、编程之类的，所以也不知道原理；这个其实是我在用[ChatWaifu](https://github.com/cjyaddone/ChatWaifu)的时候想到的，因此甚至干脆就沿用了大佬的`requirements.txt`和环境配置方法。貌似是通过模拟鼠标点击来访问ChatGPT，这个过程需要你提供ChatGPT token或者你的账号及密码(这也意味着你首先需要一个ChatGPT的账号)。
- 使用`win32clipboard`读取到剪切板内最新的内容，然后发送到ChatGPT请求翻译，这个请求具体来说大概是长下面这个样子的，你可以自己修改，让ChatGPT更准确或者更快速的执行你的指令。
```
while True:
    if i%50 == 0:
        resp = api.send_message("将以下内容翻译成中文(这些待翻译的内容都是相互连续的，句子前有方括号的是相应角色说出来的话，但是其紧挨着的下一到两个待翻译内容有可能也是这个角色说的话，而其他的没有方括号的则是主人公的想法或描述性语句，翻译时请注意前后语义的连贯)："+recent_txt)
    else:
        resp = api.send_message("翻译："+recent_txt)
    i = i+1
```
*因为ChatGPT读取有上限，翻译到后面就会忘掉最开始的指令，因此设置了每50次重新申明一遍*
- 事实上这个方法很慢，从打开到连接再到翻译，每一步都卡的离谱，你如果有更好的方法，我会很高兴的。
# 安装环境
> 安装Python>=3.7
> 
> 安装MisakaHookFinder
> 
> 安装Google Chrome浏览器
> 
> 正确的网络连接、ChatGPT账号

### 创建python虚拟环境
可以直接运行`Install.bat`(直接运行则无需以下操作)。

也可以在你的项目目录下打开cmd,手动输入代码，NAME是你的虚拟环境的名称，可以随意取。
```
python -m venv NAME
```

进入虚拟环境
```
.\NAME\Scripts\activate.bat
```

安装依赖
```
pip install -r requiremnets.txt
```

这可能需要一些时间，你可以使用国内镜像源，这样会快一些`pip install -r requiremnets.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`

### 登录你的账号
鉴于每次手动输入、复制粘贴token极其麻烦，因此，你需要在`GPT_Trans.py`中手动修改源代码，之后就不需要每次启动都重复输入账号或token了。
在`GPT_Trans.py`中找到如下代码(没有相关的软件无所谓，用txt记事本打开都可以)
```
session_token = "<your ChatGPT token>"
#api = ChatGPT(auth_type='google', email='example@gmail.com', password='password')
api = ChatGPT(session_token)
```
如果你想用账号登录，就把中间那行的#删掉，在下面那行前面加一个#，然后分别把`auth_type=` `email=` `password=`改成你的。

如果你想用token登录，那就不用管#，把\<your ChatGPT token\>换成你的token即可，具体token获取方法可以参考[ChatWaifu](https://github.com/cjyaddone/ChatWaifu)或者网上教程。

# 使用
### 确保你的剪切板最新内容是待翻译的句子
打开你的生肉galgame，运行MisakaHookFinder，使用方法参考[MisakaHookFinder](https://github.com/hanmin0822/MisakaHookFinder)或者网上教程，确保你的剪切板内是正确的内容。

你也可以用这个作为其他用途，但是总之，确保剪切板里最新内容是你需要的，因为运行`GPT_Trans.py`后，就会直接读取你的剪切板，然后发送到ChatGPT，如果内容不对的话，就会干扰到后续的使用。

### 运行
你可以直接运行`Activate.bat`(直接运行则无需以下操作)。

也可以在你的项目目录下打开cmd,手动输入代码，进入你创建的虚拟环境
```
.\NAME\Scripts\activate.bat
```

运行`GPT_Trans.py`
```
python GPT_Trans.py
```

这可能需要一些时间，请耐心等待，不要认为是卡了，特别是网络不流畅的时候，你需要等**非常**久

# 此外
这些其实很多都是我从[ChatWaifu](https://github.com/cjyaddone/ChatWaifu)的源代码上扣下来的，有很多我也不知道是什么原理，看得懂的不妨自己修改修改吧。

特别是`requirements.txt`，我只删掉了其中一些明显是用来处理声音的依赖，剩下的都原封不动的搬过来了，有懂的完全可以自己来。

# 鸣谢
- [MisakaHookFinder](https://github.com/hanmin0822/MisakaHookFinder)
- [ChatWaifu](https://github.com/cjyaddone/ChatWaifu)
- [pyChatGPT](https://github.com/terry3041/pyChatGPT)
