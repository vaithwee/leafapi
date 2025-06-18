# 🚀 PythonAnywhere 部署指南

## 准备工作

确保您已经：
- 注册了PythonAnywhere账户
- 项目在本地测试正常
- 有项目的完整代码

## 步骤1: 上传代码到PythonAnywhere

### 方法A: 使用Git（推荐）

1. 将代码推送到GitHub/GitLab
2. 在PythonAnywhere的Bash控制台中：

```bash
# 进入主目录
cd ~

# 克隆仓库（替换为您的仓库地址）
git clone https://github.com/yourusername/leafapi.git
cd leafapi
```

### 方法B: 直接上传文件

1. 在PythonAnywhere控制面板，进入 **Files** 页面
2. 创建目录：`/home/yourusername/leafapi/`
3. 上传所有项目文件到该目录

## 步骤2: 设置虚拟环境

在PythonAnywhere的**Bash控制台**中运行：

```bash
# 进入项目目录
cd ~/leafapi

# 检查Python版本
python3.10 --version

# 创建虚拟环境
python3.10 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 确认虚拟环境激活（提示符应该有(venv)前缀）
which python
```

## 步骤3: 安装依赖

```bash
# 确保在虚拟环境中
source venv/bin/activate  # 如果还没激活

# 升级pip
pip install --upgrade pip

# 安装项目依赖
pip install -r requirements.txt

# 验证安装
pip list
```

## 步骤4: 创建Web应用

1. 在PythonAnywhere控制面板，进入 **Web** 页面
2. 点击 **Add a new web app**
3. 选择域名（免费用户使用 `yourusername.pythonanywhere.com`）
4. 选择 **Manual configuration**
5. 选择 **Python 3.10**

## 步骤5: 配置Web应用设置

在Web应用配置页面中：

### 5.1 设置虚拟环境
- **Virtualenv** 字段填入：`/home/yourusername/leafapi/venv/`
- 点击勾号保存

### 5.2 设置源代码目录
- **Source code** 字段填入：`/home/yourusername/leafapi/`
- 点击勾号保存

## 步骤6: 配置WSGI文件

1. 在Web应用配置页面，找到 **Code** 部分
2. 点击 **WSGI configuration file** 链接
3. **完全替换**文件内容为：

```python
import sys
import os

# 添加项目路径到Python路径
project_home = '/home/yourusername/leafapi'  # 替换yourusername为您的用户名
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# 激活虚拟环境
activate_this = '/home/yourusername/leafapi/venv/bin/activate_this.py'
try:
    with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))
except FileNotFoundError:
    pass  # 如果activate_this.py不存在，忽略错误

# 导入FastAPI应用
from main import app

# WSGI应用
application = app
```

**重要**: 将所有的 `yourusername` 替换为您的实际PythonAnywhere用户名！

4. 保存文件（Ctrl+S）

## 步骤7: 重启Web应用

1. 返回Web应用配置页面
2. 点击绿色的 **Reload** 按钮
3. 等待重启完成

## 步骤8: 测试应用

1. 访问您的域名：`https://yourusername.pythonanywhere.com`
2. 应该看到欢迎页面
3. 测试API文档：`https://yourusername.pythonanywhere.com/docs`
4. 测试健康检查：`https://yourusername.pythonanywhere.com/health`

## 🔧 故障排除

### 问题1: 500 Internal Server Error

**解决方案**：
1. 检查错误日志：Web应用配置页面的 **Log files** 部分
2. 查看 **Error log** 获取详细错误信息

### 问题2: 模块导入错误

```bash
# 在Bash控制台中测试
cd ~/leafapi
source venv/bin/activate
python -c "from main import app; print('导入成功')"
```

### 问题3: 依赖包问题

```bash
# 重新安装依赖
cd ~/leafapi
source venv/bin/activate
pip install -r requirements.txt --force-reinstall
```

### 问题4: WSGI文件路径错误

确保WSGI文件中的路径正确：
- 将 `yourusername` 替换为实际用户名
- 路径使用绝对路径
- 检查文件权限

## 📝 部署检查清单

- [ ] 代码已上传到PythonAnywhere
- [ ] 虚拟环境已创建并激活
- [ ] 依赖包已安装
- [ ] Web应用已创建（Python 3.10）
- [ ] 虚拟环境路径已设置
- [ ] 源代码路径已设置
- [ ] WSGI文件已正确配置
- [ ] 用户名已在WSGI文件中替换
- [ ] Web应用已重启
- [ ] 应用可以访问

## 🔄 更新部署

当您更新代码时：

```bash
# 如果使用Git
cd ~/leafapi
git pull origin main

# 如果需要更新依赖
source venv/bin/activate
pip install -r requirements.txt

# 重启Web应用（在控制面板中点击Reload）
```

## 🌐 域名配置

免费用户默认域名：`yourusername.pythonanywhere.com`

如需自定义域名，需要升级到付费计划。

## 📞 获取帮助

如果遇到问题：
1. 查看PythonAnywhere官方文档
2. 检查错误日志
3. 在PythonAnywhere论坛寻求帮助
4. 联系PythonAnywhere支持

---
**部署完成后，您的FastAPI应用就可以通过互联网访问了！** 🎉 