# LeafAPI - FastAPI项目

一个基于FastAPI的现代化Web API项目，支持部署到PythonAnywhere。

## 特性

- ✨ 基于FastAPI构建，支持异步处理
- 🚀 自动API文档生成（Swagger UI）
- 🔒 CORS支持，可配置跨域访问
- 📦 完整的CRUD操作示例
- 🐍 Python 3.10兼容
- 🌐 可直接部署到PythonAnywhere

## 项目结构

```
leafapi/
├── main.py              # FastAPI主应用
├── wsgi.py             # PythonAnywhere WSGI配置
├── config.py           # 配置文件
├── requirements.txt    # 依赖包
└── README.md          # 项目文档
```

## 本地开发

### 环境要求

- Python 3.10+
- pip

### 安装依赖

```bash
# 克隆项目
git clone <your-repo-url>
cd leafapi

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或者
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

### 运行应用

```bash
# 方式1: 使用启动脚本（推荐）
python start.py                    # 开发模式（默认）
python start.py --env dev          # 开发模式（热重载）
python start.py --env prod         # 生产模式
python start.py --port 8080        # 指定端口

# 方式2: 直接运行
python main.py

# 方式3: 使用uvicorn命令
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

访问以下地址：
- 应用首页: http://localhost:8000
- 交互式API文档: http://localhost:8000/docs
- ReDoc文档: http://localhost:8000/redoc
- 健康检查: http://localhost:8000/health

## API端点

### 基础端点
- `GET /` - 根路径，返回欢迎信息
- `GET /health` - 健康检查

### 项目管理端点
- `GET /items` - 获取所有项目
- `GET /items/{item_id}` - 获取特定项目
- `POST /items` - 创建新项目
- `PUT /items/{item_id}` - 更新项目
- `DELETE /items/{item_id}` - 删除项目

### 请求示例

```bash
# 创建项目
curl -X POST "http://localhost:8000/items" \
     -H "Content-Type: application/json" \
     -d '{"name": "测试项目", "description": "这是一个测试项目", "price": 99.99}'

# 获取所有项目
curl "http://localhost:8000/items"
```

## 部署到PythonAnywhere

### 步骤1: 上传代码

1. 将项目代码上传到PythonAnywhere的Files页面
2. 建议上传到 `/home/yourusername/leafapi/` 目录

### 步骤2: 安装依赖

在PythonAnywhere的Bash控制台中：

```bash
# 进入项目目录
cd ~/leafapi

# 创建虚拟环境
python3.10 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 步骤3: 配置Web应用

1. 在PythonAnywhere控制面板中创建新的Web应用
2. 选择"Manual configuration"
3. 选择Python 3.10

### 步骤4: 配置WSGI文件

编辑 `/var/www/yourusername_pythonanywhere_com_wsgi.py` 文件：

```python
import sys
import os

# 添加项目路径
project_home = '/home/yourusername/leafapi'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# 激活虚拟环境
activate_this = '/home/yourusername/leafapi/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# 导入FastAPI应用
from main import app
application = app
```

### 步骤5: 配置虚拟环境

在Web应用配置页面中：
- 设置虚拟环境路径: `/home/yourusername/leafapi/venv/`

### 步骤6: 重启Web应用

点击"Reload"按钮重启Web应用。

## 配置说明

### 环境变量

可以在PythonAnywhere的环境变量中设置：

```bash
SECRET_KEY=your-production-secret-key
PYTHONANYWHERE_USERNAME=yourusername
```

### CORS配置

在 `config.py` 中修改 `CORS_ORIGINS` 以适应你的前端应用：

```python
CORS_ORIGINS: List[str] = [
    "https://yourdomain.com",
    "https://www.yourdomain.com"
]
```

## 开发建议

### 添加新功能

1. 在 `main.py` 中添加新的路由
2. 创建相应的Pydantic模型
3. 更新API文档

### 数据库集成

如需添加数据库支持，推荐使用SQLAlchemy：

```bash
pip install sqlalchemy alembic
```

### 测试

添加测试文件：

```bash
pip install pytest httpx
```

创建 `test_main.py`:

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "欢迎使用LeafAPI" in response.json()["message"]
```

## 常见问题

### 1. 导入错误
确保所有文件都在正确的目录中，并且虚拟环境已正确激活。

### 2. 端口问题
PythonAnywhere会自动处理端口配置，无需修改。

### 3. 静态文件
如需提供静态文件，可以使用FastAPI的StaticFiles中间件。

## 许可证

MIT License

## 贡献

欢迎提交Pull Request和Issue！

---

📧 如有问题，请联系开发者。 