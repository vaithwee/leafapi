import sys
import os

# 添加项目路径到Python路径
project_home = '/home/yourusername/leafapi'  # 请替换为你的PythonAnywhere用户名
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# 导入FastAPI应用
from main import app

# WSGI应用
application = app 