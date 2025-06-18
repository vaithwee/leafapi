#!/usr/bin/env python3
"""
PythonAnywhere WSGI配置文件
请将 'yourusername' 替换为您的实际PythonAnywhere用户名

使用方法：
1. 复制此文件的内容
2. 替换所有的 'yourusername' 为您的真实用户名
3. 粘贴到PythonAnywhere的WSGI配置文件中
"""

import sys
import os

# ===== 重要：请替换 yourusername 为您的实际用户名 =====
USERNAME = 'yourusername'  # 请修改这里！

# 添加项目路径到Python路径
project_home = f'/home/{USERNAME}/leafapi'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# 激活虚拟环境
activate_this = f'/home/{USERNAME}/leafapi/venv/bin/activate_this.py'
try:
    with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))
    print(f"✅ 虚拟环境已激活: {activate_this}")
except FileNotFoundError:
    print(f"⚠️  activate_this.py 未找到，跳过虚拟环境激活")
    print(f"   路径: {activate_this}")
    pass

# 设置环境变量（可选）
os.environ.setdefault('PYTHONPATH', project_home)

try:
    # 导入FastAPI应用
    from main import app
    print("✅ FastAPI应用导入成功")
    
    # WSGI应用
    application = app
    print("✅ WSGI应用配置完成")
    
except ImportError as e:
    print(f"❌ 导入错误: {e}")
    print(f"   项目路径: {project_home}")
    print(f"   Python路径: {sys.path}")
    
    # 创建一个简单的测试应用
    def application(environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)
        error_msg = f"FastAPI应用导入失败: {str(e)}\n项目路径: {project_home}"
        return [error_msg.encode('utf-8')]

# 调试信息
print(f"📍 项目路径: {project_home}")
print(f"🐍 Python版本: {sys.version}")
print(f"📦 Python路径: {sys.path[:3]}...")  # 只显示前3个路径 