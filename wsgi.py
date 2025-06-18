"""
WSGI 配置文件用于PythonAnywhere部署
"""

import sys
import os
import traceback

# 添加项目路径到Python路径
project_home = '/home/leafapi/leafapi'  # 请替换为您的实际用户名和项目路径
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# 设置环境变量
os.environ.setdefault('PYTHONPATH', project_home)

# 初始化应用变量
application = None
import_error = None

try:
    # 导入FastAPI应用
    from main import app
    
    # 使用asgiref将ASGI应用转换为WSGI
    from asgiref.wsgi import WsgiToAsgi
    
    # 创建WSGI应用
    application = WsgiToAsgi(app)
    
except Exception as e:
    # 保存详细错误信息
    import_error = f"错误: {str(e)}\n\n详细信息:\n{traceback.format_exc()}"
    
    # 如果导入失败，创建一个简单的错误应用
    def application(environ, start_response):
        response_body = f'LeafAPI 导入失败:\n\n{import_error}'.encode('utf-8')
        status = '500 Internal Server Error'
        response_headers = [('Content-Type', 'text/plain; charset=utf-8'),
                           ('Content-Length', str(len(response_body)))]
        start_response(status, response_headers)
        return [response_body] 