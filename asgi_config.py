"""
PythonAnywhere ASGI 配置文件
用于 FastAPI 在 PythonAnywhere 上的部署
"""

import os
import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# 从 main.py 导入 FastAPI 应用
from main import app

# 设置环境变量
os.environ.setdefault("ENVIRONMENT", "production")

# ASGI 应用对象
application = app

if __name__ == "__main__":
    # 本地测试用
    import uvicorn
    uvicorn.run(
        "asgi_config:application",
        host="0.0.0.0",
        port=8000,
        reload=False
    ) 