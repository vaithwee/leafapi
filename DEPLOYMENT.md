# PythonAnywhere 部署指南

## 前提条件
- PythonAnywhere账户
- Python 3.8+ 环境

## 部署步骤

### 1. 上传代码
将项目文件上传到PythonAnywhere，例如：
```
/home/your_username/leafapi/
├── main.py
├── wsgi.py
├── requirements.txt
└── config.py
```

### 2. 安装依赖
在PythonAnywhere的Bash控制台中：
```bash
cd ~/leafapi
pip3.8 install --user -r requirements.txt
```

### 3. 配置Web应用
1. 进入PythonAnywhere的Web标签页
2. 点击"Add a new web app"
3. 选择"Manual configuration"
4. 选择Python版本（建议3.8+）

### 4. 配置WSGI文件路径
在Web应用配置页面：
- 将"Source code"路径设置为：`/home/your_username/leafapi`
- 将"WSGI configuration file"路径设置为：`/home/your_username/leafapi/wsgi.py`

### 5. 编辑WSGI配置
1. 打开wsgi.py文件
2. 将`your_username`替换为您的实际用户名
3. 确保路径正确

### 6. 重新加载Web应用
在Web标签页点击"Reload"按钮

## 测试部署
访问以下URL测试应用：
- 主页：`https://your_username.pythonanywhere.com/`
- API文档：`https://your_username.pythonanywhere.com/docs`
- 健康检查：`https://your_username.pythonanywhere.com/health`

## 故障排除

### 常见问题
1. **导入错误**：检查Python路径和依赖安装
2. **404错误**：确认WSGI文件路径正确
3. **500错误**：查看错误日志（在Web标签页的Error log中）

### 调试技巧
- 查看错误日志：Web标签页 → Error log
- 测试导入：在控制台中运行 `python3.8 -c "from main import app; print('导入成功')"`

## 注意事项
- PythonAnywhere免费账户有一些限制（如外部API访问）
- 确保所有依赖都已正确安装
- 如需使用外部数据库，需要配置相应的连接参数 