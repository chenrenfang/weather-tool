# -*- coding: utf-8 -*-
# 天气接口的自动检查（pytest）
# 运行：E:\Python311\python.exe -m pytest E:\PythonProjects\weather_tool\test_weather.py -v
# 作用：程序自己验证接口是否正常，不用人肉盯着看

import requests

import weather  # 导入我们写的 weather.py


def test_query_normal_city():
    """正常城市：能查到非空天气，且带温度符号"""
    result = weather.get_weather("重庆")
    assert result                 # 结果不能是空的
    assert "°" in result          # 结果里应该有温度符号 °


def test_api_status_200():
    """接口本身：直接请求接口，返回状态码必须是 200（正常）"""
    resp = requests.get(
        "https://wttr.in/重庆",
        params={"format": "%c %t %w", "lang": "zh"},
        timeout=10,
    )
    assert resp.status_code == 200


def test_unknown_city_returns_friendly_message():
    """异常城市：返回的是友好提示，而不是程序崩溃"""
    result = weather.get_weather("不存在的城市xyz123")
    assert "查询失败" in result
