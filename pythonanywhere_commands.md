# PythonAnywhere FastAPI 管理命令参考

## 基本信息
- **项目名称**: LeafAPI
- **框架**: FastAPI
- **服务器**: Uvicorn (ASGI)
- **Python版本**: 3.10

## 手动部署步骤

### 1. 安装命令行工具
```bash
pip install --upgrade pythonanywhere
```

### 2. 创建虚拟环境
```bash
mkvirtualenv leafapi_env --python=python3.10
```

### 3. 安装依赖
```bash
source ~/.virtualenvs/leafapi_env/bin/activate
pip install -r requirements.txt
pip install "uvicorn[standard]"
```

### 4. 创建网站 (替换 YOURUSERNAME)
```bash
pa website create --domain YOURUSERNAME.pythonanywhere.com --command '/home/YOURUSERNAME/.virtualenvs/leafapi_env/bin/uvicorn --app-dir /home/YOURUSERNAME/leafapi --uds ${DOMAIN_SOCKET} main:app'
```

## 常用管理命令

### 网站管理
```bash
# 查看所有网站
pa website get

# 查看特定网站详情
pa website get --domain YOURUSERNAME.pythonanywhere.com

# 重新加载网站 (代码更新后必须执行)
pa website reload --domain YOURUSERNAME.pythonanywhere.com

# 删除网站
pa website delete --domain YOURUSERNAME.pythonanywhere.com
```

### 日志查看
```bash
# 查看错误日志
tail -f /var/log/YOURUSERNAME.pythonanywhere.com.error.log

# 查看服务器日志
tail -f /var/log/YOURUSERNAME.pythonanywhere.com.server.log

# 查看访问日志
tail -f /var/log/YOURUSERNAME.pythonanywhere.com.access.log
```

### 自定义域名 (付费功能)
```bash
# 创建自定义域名网站
pa website create --domain yourdomain.com --command 'COMMAND_HERE'

# 创建 SSL 证书
pa website create-autorenew-cert --domain yourdomain.com
```

## 启动命令详解

完整的启动命令格式：
```bash
/home/YOURUSERNAME/.virtualenvs/leafapi_env/bin/uvicorn --app-dir /home/YOURUSERNAME/leafapi --uds ${DOMAIN_SOCKET} main:app
```

参数说明：
- `/home/YOURUSERNAME/.virtualenvs/leafapi_env/bin/uvicorn`: 虚拟环境中的 uvicorn 路径
- `--app-dir /home/YOURUSERNAME/leafapi`: 项目代码目录
- `--uds ${DOMAIN_SOCKET}`: 使用 Unix Domain Socket（PythonAnywhere 要求）
- `main:app`: 从 main.py 文件导入 app 对象

## 访问地址

部署成功后，您的应用将在以下地址可用：
- **主页**: https://YOURUSERNAME.pythonanywhere.com/
- **API 文档**: https://YOURUSERNAME.pythonanywhere.com/docs
- **ReDoc 文档**: https://YOURUSERNAME.pythonanywhere.com/redoc
- **健康检查**: https://YOURUSERNAME.pythonanywhere.com/health

## 故障排除

### 常见问题
1. **网站显示 404**: 等待几秒钟后刷新页面
2. **Import 错误**: 检查虚拟环境路径和依赖安装
3. **权限错误**: 确保文件权限正确

### 调试步骤
1. 检查错误日志: `tail -f /var/log/YOURUSERNAME.pythonanywhere.com.error.log`
2. 验证虚拟环境: `ls -la ~/.virtualenvs/leafapi_env/bin/`
3. 测试启动命令: 在 bash 中手动运行启动命令
4. 检查项目文件: 确保 main.py 存在且语法正确

## 代码更新流程
1. 上传新代码到 PythonAnywhere
2. 执行重新加载命令: `pa website reload --domain YOURUSERNAME.pythonanywhere.com`
3. 检查日志确认更新成功

## 限制说明
- 静态文件映射暂不支持
- ASGI 功能处于测试阶段
- 免费账户有资源限制 