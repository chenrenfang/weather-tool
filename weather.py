"""
天气查询小工具（我的第一个 Python 作品 · 第 3 版 · 带保质期缓存）

用法：
    运行程序后输入城市名（如：重庆），回车即可查看天气。
    支持异常处理和 pytest 自动化测试。
    升级：缓存带“保质期”（TTL），10 分钟内重复查询不联网，过期自动重新查询。
"""

import requests
import time  # 时间模块：用来给缓存记“保质期”

# 缓存保质期：600 秒 = 10 分钟
EXPIRE_TIME = 600

# 缓存小本本：存“查过的城市 → {“weather”: 天气结果, “query_time”: 查询时间}”
weather_cache = {}


def get_weather(city):
    """根据城市名，返回一行天气文字；失败时返回友好提示"""
    # 第 1 步：翻小本本，看这个城市查过没
    if city in weather_cache:
        cache_data = weather_cache[city]
        # 算一算：现在的时间 - 上次查询的时间 = 缓存放了多久
        time_passed = time.time() - cache_data["query_time"]

        # 没过期：直接用本子里的结果，不联网
        if time_passed < EXPIRE_TIME:
            print(f"[缓存命中] {city} 的天气是 10 分钟内查的，直接读取，未联网")
            return cache_data["weather"]
        # 过期了：不返回，继续往下走，重新联网查
        print(f"[缓存过期] {city} 的数据太旧了，重新联网查询...")

    url = f"https://wttr.in/{city}"
    params = {"format": "%c %t %w", "lang": "zh"}  # 参数交给 params 自动编码
    try:
        resp = requests.get(url, params=params, timeout=10)  # 发请求，最多等10秒
        resp.raise_for_status()  # 请求失败就抛出异常
        result = resp.text.strip()  # 去掉首尾空白

        # 第 2 步：更新小本本 = “天气结果 + 查询时间”两条信息
        weather_cache[city] = {
            "weather": result,
            "query_time": time.time()
        }
        return result
    except requests.RequestException:
        return "查询失败：请检查网络，或确认城市名拼写"


if __name__ == "__main__":
    print("=== 欢迎使用天气查询小工具（输入 q 退出）===")
    while True:
        city = input("\n请输入城市名（如：重庆）：").strip()

        if city.lower() == "q":
            print("感谢使用，再见！")
            break

        if not city:
            print("城市名不能为空哦！")
            continue

        print(f"{city} 的天气：{get_weather(city)}")
