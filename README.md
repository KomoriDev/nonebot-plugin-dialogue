<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-dialogue

_✨ NoneBot 反馈插件 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/owner/nonebot-plugin-dialogue.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-dialogue">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-dialogue.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

可以跨越时空与管理员对话

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-dialogue

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-dialogue
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-dialogue
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-dialogue
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-dialogue
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_dialogue"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置。在这里，我们以 `/` 为前缀来举例
```
COMMAND_START=["/"]
```

## 🎉 使用

### 群员
```
/对话超管 [内容]
```

### 超管
查看当前存储的消息
```
/t
```

在群内回复指定用户
```
/t [qq] [group] [文本]
```

在群内发送消息
```
/t -1 [group] [文本]
```

回复指定id的对话，id在 `/t` 中获取
```
/t [id] [文本]
```

私聊用户
```
/t [qq] [文本]
```

## 🙏鸣谢

* [`HibiKier/zhenxun_bot`](https://github.com/HibiKier/zhenxun_bot/) 本项目直接参考 ~~（直接开抄）~~
