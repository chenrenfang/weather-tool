"""
天气查询小工具 · Web 版（我的第一个 Flask 作品）

运行后浏览器打开 http://127.0.0.1:5000 就能查天气
"""

from flask import Flask, request
import weather  # 复用上一版写好的 get_weather

app = Flask(__name__)


# 第 1 个地址：/ （网站的根），显示查询页面
@app.route("/")
def index():
    return """
    <h1>天气查询小工具</h1>
    <form action="/weather" method="get">
        <input name="city" placeholder="输入城市名，如：重庆">
        <button type="submit">查询</button>
    </form>
    """


# 第 2 个地址：/weather?city=重庆，真正干活的地方
@app.route("/weather")
def weather_page():
    city = request.args.get("city", "")  # 从网址里取出城市名
    result = weather.get_weather(city)   # 调用我们写好的查询函数
    return f"""
    <h2>{city} 的天气</h2>
    <p>{result}</p>
    <p><a href="/">再查一个城市</a></p>
    """


if __name__ == "__main__":
    app.run(debug=True)  # 启动网站服务器 ;本地测试开启 debug，上线部署需设为 False
