#!/usr/bin/env python3
"""
PythonAnywhere 部署准备脚本
此脚本帮助您准备部署到PythonAnywhere所需的文件

使用方法：
python3 prepare_deploy.py --username your_pythonanywhere_username
"""

import os
import argparse
import shutil
from pathlib import Path

def create_deployment_files(username):
    """创建部署所需的文件"""
    print(f"🚀 为用户 '{username}' 准备PythonAnywhere部署文件...")
    
    # 创建个性化的WSGI文件
    wsgi_content = f'''import sys
import os

# 添加项目路径到Python路径
project_home = '/home/{username}/leafapi'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# 激活虚拟环境
activate_this = '/home/{username}/leafapi/venv/bin/activate_this.py'
try:
    with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))
except FileNotFoundError:
    pass  # 如果activate_this.py不存在，忽略错误

# 导入FastAPI应用
from main import app

# WSGI应用
application = app
'''
    
    # 保存WSGI文件
    with open(f'{username}_wsgi.py', 'w', encoding='utf-8') as f:
        f.write(wsgi_content)
    print(f"✅ 已创建: {username}_wsgi.py")
    
    # 创建部署命令文件
    bash_commands = f'''#!/bin/bash
# PythonAnywhere 部署命令
# 在PythonAnywhere的Bash控制台中运行这些命令

echo "🚀 开始部署 LeafAPI 到 PythonAnywhere..."

# 进入项目目录
cd ~/leafapi

# 检查Python版本
echo "🐍 检查Python版本..."
python3.10 --version

# 创建虚拟环境
echo "📦 创建虚拟环境..."
python3.10 -m venv venv

# 激活虚拟环境
echo "⚡ 激活虚拟环境..."
source venv/bin/activate

# 升级pip
echo "🔧 升级pip..."
pip install --upgrade pip

# 安装依赖
echo "📚 安装依赖..."
pip install -r requirements.txt

# 测试导入
echo "🧪 测试应用导入..."
python -c "from main import app; print('✅ FastAPI应用导入成功')"

echo "✅ 部署准备完成！"
echo "📋 接下来的步骤："
echo "1. 在PythonAnywhere创建Web应用（Python 3.10）"
echo "2. 设置虚拟环境路径: /home/{username}/leafapi/venv/"
echo "3. 设置源代码路径: /home/{username}/leafapi/"
echo "4. 配置WSGI文件（使用 {username}_wsgi.py 的内容）"
echo "5. 重启Web应用"
'''
    
    with open(f'deploy_commands_{username}.sh', 'w', encoding='utf-8') as f:
        f.write(bash_commands)
    print(f"✅ 已创建: deploy_commands_{username}.sh")
    
    # 创建部署清单
    checklist = f'''# 🚀 PythonAnywhere 部署清单

## 用户信息
- 用户名: {username}
- 域名: https://{username}.pythonanywhere.com

## 部署步骤

### 1. 上传代码
- [ ] 代码已上传到 `/home/{username}/leafapi/`
- [ ] 所有文件都在正确位置

### 2. 虚拟环境设置
- [ ] 运行: `cd ~/leafapi`
- [ ] 运行: `python3.10 -m venv venv`
- [ ] 运行: `source venv/bin/activate`
- [ ] 运行: `pip install -r requirements.txt`

### 3. Web应用配置
- [ ] 创建了Web应用（Python 3.10）
- [ ] 设置虚拟环境: `/home/{username}/leafapi/venv/`
- [ ] 设置源代码路径: `/home/{username}/leafapi/`

### 4. WSGI配置
- [ ] 复制了 `{username}_wsgi.py` 的内容到WSGI文件
- [ ] 保存了WSGI文件

### 5. 测试
- [ ] 重启了Web应用
- [ ] 访问 https://{username}.pythonanywhere.com
- [ ] 测试 https://{username}.pythonanywhere.com/docs
- [ ] 测试 https://{username}.pythonanywhere.com/health

## 故障排除

如果遇到问题，检查：
1. 错误日志（Web应用配置页面）
2. 路径是否正确
3. 虚拟环境是否激活
4. 依赖是否安装完成

## 更新部署

更新代码时：
```bash
cd ~/leafapi
git pull origin main  # 如果使用Git
# 或重新上传文件
source venv/bin/activate
pip install -r requirements.txt
# 然后在控制面板重启Web应用
```
'''
    
    with open(f'deployment_checklist_{username}.md', 'w', encoding='utf-8') as f:
        f.write(checklist)
    print(f"✅ 已创建: deployment_checklist_{username}.md")
    
    print(f"\n🎉 部署文件准备完成！")
    print(f"📁 创建的文件：")
    print(f"   - {username}_wsgi.py (复制到PythonAnywhere的WSGI文件)")
    print(f"   - deploy_commands_{username}.sh (在Bash控制台运行)")
    print(f"   - deployment_checklist_{username}.md (部署检查清单)")

def main():
    parser = argparse.ArgumentParser(description="准备PythonAnywhere部署文件")
    parser.add_argument(
        "--username", 
        required=True,
        help="您的PythonAnywhere用户名"
    )
    
    args = parser.parse_args()
    
    # 验证用户名
    if not args.username or args.username == 'yourusername':
        print("❌ 请提供您的真实PythonAnywhere用户名")
        print("例如: python3 prepare_deploy.py --username myusername")
        return
    
    create_deployment_files(args.username)

if __name__ == "__main__":
    main() 