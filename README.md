# Weather Tool（天气查询小工具）

一个用 Python 调用免费天气接口的入门项目，支持命令行交互与 Web 网页两种使用方式。项目内置 TTL 缓存机制，并配套 pytest 接口自动化测试。

## 功能特色

- 双端体验：既可以在终端直接查询，也可以在浏览器中通过 Web 页面查询
- TTL 缓存机制：内置 10 分钟"保质期"缓存，短时间内重复查询同一城市不消耗网络，秒出结果
- 防崩溃设计：断网或城市名输入错误时返回友好提示，程序不会直接报错崩溃
- 自动化测试：使用 pytest 编写接口测试用例，一键验证程序稳定性
- 优雅退出：命令行版本支持循环查询，输入 q 即可退出

## 技术栈

- Python 3.11
- requests（网络请求库）
- Flask（轻量级 Web 框架）
- pytest（自动化测试框架）
- time（用于实现 TTL 缓存）

## 项目结构

```text
weather_tool/
├── weather.py          # 核心逻辑（包含天气查询与本地缓存机制）
├── app.py              # Web 版入口（Flask 应用）
├── test_weather.py     # pytest 自动化测试文件
├── requirements.txt    # 项目依赖清单
├── .gitignore          # Git 忽略文件配置
└── README.md           # 项目说明文档
```

## 快速开始

克隆项目并安装依赖：

```bash
pip install -r requirements.txt
```

### 方式一：命令行版

运行主程序：

```bash
python weather.py
```

根据提示输入城市名（如：重庆、彭水），回车即可看到天气。输入 q 退出程序。

### 方式二：Web 网页版（Flask）

启动 Web 服务器：

```bash
python app.py
```

在浏览器中打开 http://127.0.0.1:5000，即可在网页中输入城市名查询天气。

## 运行测试

本项目包含 3 个测试用例，覆盖正常查询、接口状态及异常处理。

查看每个用例的执行情况：

```bash
python -m pytest test_weather.py -v
```

只看最终结果：

```bash
python -m pytest test_weather.py -q
```

## 测试用例覆盖

- 正常城市：能查到非空天气，且包含温度符号 °
- 接口状态：直接请求接口，返回状态码必须为 200
- 异常城市：输入乱码城市（如 xyz123），返回"查询失败"友好提示，而非程序崩溃