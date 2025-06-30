from flask import Flask

app = Flask(__name__)

@app.route('/')  # 定义根路由
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>我的第一个Flask网页</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
            h1 { color: navy; }
        </style>
    </head>
    <body>
        <h1>你好，世界！👋</h1>
        <p>这是我的第一个用 Python Flask 框架创建的网页！</p >
        <p>关于我</p >
    </body>
    </html>
    """

@app.route('/about')
def about():
    return """
    <h1>关于这个页面</h1>
    <p>这是用不到10行Python代码（不算HTML）创建的！</p >
    <p>返回首页</p >
    """

if __name__ == '__main__':
    app.run(debug=True)  # 启动开发服务器