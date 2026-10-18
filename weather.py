"""
天气查询小工具（我的第一个 Python 作品 · 第 2 版）

用法：
    运行程序后输入城市名（如：重庆），回车即可查看天气。
    支持异常处理和 pytest 自动化测试。
"""

import requests


def get_weather(city):
    """根据城市名，返回一行天气文字；失败时返回友好提示"""
    url = f"https://wttr.in/{city}"
    params = {"format": "%c %t %w", "lang": "zh"}  # 参数交给 params 自动编码
    try:
        resp = requests.get(url, params=params, timeout=10)  # 发请求，最多等10秒
        resp.raise_for_status()  # 请求失败就抛出异常
        return resp.text.strip()  # 去掉首尾空白再返回
    except requests.RequestException:
        return "查询失败：请检查网络，或确认城市名拼写"


if __name__ == "__main__":
    city = input("请输入城市名（如：重庆）：")
    print(f"{city} 的天气：{get_weather(city)}")
