#!/bin/bash

# PythonAnywhere FastAPI 部署脚本
# 使用方法: chmod +x start_pythonanywhere.sh && ./start_pythonanywhere.sh

set -e  # 遇到错误时停止执行

# 配置变量
VENV_NAME="leafapi_env"
PROJECT_DIR="leafapi"
USERNAME=$(whoami)

echo "=== PythonAnywhere FastAPI 部署脚本 ==="
echo "用户名: $USERNAME"
echo "项目目录: $PROJECT_DIR"
echo "虚拟环境: $VENV_NAME"
echo ""

# 1. 创建虚拟环境
echo "步骤 1: 创建虚拟环境..."
if [ ! -d "/home/$USERNAME/.virtualenvs/$VENV_NAME" ]; then
    mkvirtualenv $VENV_NAME --python=python3.10
    echo "✅ 虚拟环境创建成功"
else
    echo "✅ 虚拟环境已存在"
fi

# 2. 激活虚拟环境并安装依赖
echo "步骤 2: 安装项目依赖..."
source /home/$USERNAME/.virtualenvs/$VENV_NAME/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install "uvicorn[standard]"
echo "✅ 依赖安装完成"

# 3. 检查项目文件
echo "步骤 3: 检查项目文件..."
if [ ! -f "main.py" ]; then
    echo "❌ 错误: main.py 文件不存在"
    exit 1
fi
echo "✅ 项目文件检查通过"

# 4. 创建网站
echo "步骤 4: 创建 PythonAnywhere 网站..."
DOMAIN="$USERNAME.pythonanywhere.com"
COMMAND="/home/$USERNAME/.virtualenvs/$VENV_NAME/bin/uvicorn --app-dir /home/$USERNAME/$PROJECT_DIR --uds \${DOMAIN_SOCKET} main:app"

echo "域名: $DOMAIN"
echo "启动命令: $COMMAND"

# 使用 pa 命令创建网站
pa website create --domain $DOMAIN --command "$COMMAND"

if [ $? -eq 0 ]; then
    echo "✅ 网站创建成功！"
    echo ""
    echo "🌐 您的网站现在可以通过以下地址访问:"
    echo "   https://$DOMAIN"
    echo "   API 文档: https://$DOMAIN/docs"
    echo "   ReDoc 文档: https://$DOMAIN/redoc"
    echo ""
    echo "📝 常用命令:"
    echo "   重新加载网站: pa website reload --domain $DOMAIN"
    echo "   查看网站状态: pa website get --domain $DOMAIN"
    echo "   查看日志: tail -f /var/log/$DOMAIN.error.log"
    echo ""
else
    echo "❌ 网站创建失败，请检查错误信息"
    exit 1
fi

echo "=== 部署完成 ===" 