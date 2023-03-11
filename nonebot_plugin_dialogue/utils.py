from typing import Union, List

from nonebot.adapters.onebot.v11 import Message

try:
    import ujson as json
except ModuleNotFoundError:
    import json

def is_number(s: Union[int, str]) -> bool:
    """
    说明:
        检测 s 是否为数字
    参数:
        :param s: 文本
    """
    if isinstance(s, int):
        return True
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata

        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False



def get_message_img(data: Union[str, Message]) -> List[str]:
    """
    说明:
        获取消息中所有的 图片 的链接
    参数:
        :param data: event.json()
    """
    img_list = []
    if isinstance(data, str):
        event = json.loads(data)
        if data and (message := event.get("message")):
            for msg in message:
                if msg["type"] == "image":
                    img_list.append(msg["data"]["url"])
    else:
        for seg in data["image"]:
            img_list.append(seg.data["url"])
    return img_list