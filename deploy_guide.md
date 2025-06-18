# PythonAnywhere FastAPI 部署指南

## 🚀 快速部署

### 方法一：使用自动化脚本 (推荐)
1. 上传项目文件到 PythonAnywhere
2. 在 Bash 控制台中执行：
```bash
cd ~/leafapi
chmod +x start_pythonanywhere.sh
./start_pythonanywhere.sh
```

### 方法二：手动部署
按照 `pythonanywhere_commands.md` 中的步骤逐步执行。

## 📋 部署前准备

### 1. 确保项目文件完整
- ✅ `main.py` - FastAPI 应用主文件
- ✅ `requirements.txt` - 依赖列表
- ✅ `config.py` - 配置文件
- ✅ `asgi_config.py` - ASGI 配置 (可选)

### 2. 检查依赖文件
确保 `requirements.txt` 包含以下核心依赖：
```
fastapi
uvicorn[standard]
pydantic
python-multipart
```

### 3. 验证应用代码
确保 `main.py` 中的 FastAPI 应用对象名为 `app`：
```python
app = FastAPI(...)
```

## 🔧 配置说明

### 虚拟环境配置
- **环境名称**: `leafapi_env`
- **Python版本**: 3.10
- **位置**: `/home/USERNAME/.virtualenvs/leafapi_env/`

### 启动命令模板
```bash
/home/USERNAME/.virtualenvs/leafapi_env/bin/uvicorn \
  --app-dir /home/USERNAME/leafapi \
  --uds ${DOMAIN_SOCKET} \
  main:app
```

### 环境变量
PythonAnywhere 会自动设置以下环境变量：
- `DOMAIN_SOCKET`: Unix Socket 路径
- `PYTHONANYWHERE_DOMAIN`: 您的域名

## 📊 监控和维护

### 日志文件位置
- **错误日志**: `/var/log/USERNAME.pythonanywhere.com.error.log`
- **服务器日志**: `/var/log/USERNAME.pythonanywhere.com.server.log`
- **访问日志**: `/var/log/USERNAME.pythonanywhere.com.access.log`

### 监控命令
```bash
# 实时查看错误日志
tail -f /var/log/USERNAME.pythonanywhere.com.error.log

# 检查应用状态
pa website get --domain USERNAME.pythonanywhere.com

# 重启应用
pa website reload --domain USERNAME.pythonanywhere.com
```

## 🔍 故障排除

### 常见错误及解决方案

#### 1. ModuleNotFoundError
**原因**: 依赖未安装或路径问题
**解决**:
```bash
workon leafapi_env
pip install -r requirements.txt
```

#### 2. 应用无法启动
**检查步骤**:
1. 验证 `main.py` 语法: `python -m py_compile main.py`
2. 检查启动命令路径是否正确
3. 查看错误日志获取详细信息

#### 3. 502 Bad Gateway
**原因**: 应用进程崩溃
**解决**:
1. 检查错误日志
2. 重新加载应用
3. 验证代码是否有语法错误

#### 4. 导入错误
**解决**:
```bash
# 检查项目结构
ls -la ~/leafapi/
# 确保虚拟环境激活
workon leafapi_env
# 测试导入
python -c "from main import app; print('导入成功')"
```

## 🎯 性能优化

### 1. 启动配置优化
在 `main.py` 中添加生产环境配置：
```python
if os.getenv("ENVIRONMENT") == "production":
    app.debug = False
    # 其他生产环境配置
```

### 2. 日志配置
```python
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### 3. CORS 配置
生产环境应限制 CORS 域名：
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # 具体域名
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
```

## 📈 扩展功能

### 1. 自定义域名
```bash
# 创建自定义域名网站
pa website create --domain yourdomain.com --command 'COMMAND'
# 设置 SSL 证书
pa website create-autorenew-cert --domain yourdomain.com
```

### 2. 数据库集成
如需数据库支持，可以：
- 使用 SQLite (文件数据库)
- 配置 MySQL (PythonAnywhere 提供)
- 使用外部数据库服务

### 3. 定时任务
```bash
# 编辑定时任务
crontab -e
# 添加任务示例
0 2 * * * /home/USERNAME/.virtualenvs/leafapi_env/bin/python /home/USERNAME/leafapi/daily_task.py
```

## 📚 参考资源
- [PythonAnywhere ASGI 文档](https://help.pythonanywhere.com/pages/ASGICommandLine/)
- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
- [Uvicorn 配置指南](https://www.uvicorn.org/settings/)

## 🆘 获取帮助
- PythonAnywhere 论坛: https://forums.pythonanywhere.com/
- 技术支持: support@pythonanywhere.com
- FastAPI 社区: https://github.com/tiangolo/fastapi/discussions 