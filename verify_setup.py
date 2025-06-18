#!/usr/bin/env python3
"""
PythonAnywhere 部署前验证脚本
检查项目配置和依赖是否正确
"""

import sys
import os
import importlib.util
from pathlib import Path

def check_file_exists(filepath, description):
    """检查文件是否存在"""
    if Path(filepath).exists():
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description} 缺失: {filepath}")
        return False

def check_python_syntax(filepath):
    """检查 Python 文件语法"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            compile(f.read(), filepath, 'exec')
        print(f"✅ 语法检查通过: {filepath}")
        return True
    except SyntaxError as e:
        print(f"❌ 语法错误 {filepath}: {e}")
        return False
    except Exception as e:
        print(f"❌ 检查失败 {filepath}: {e}")
        return False

def check_fastapi_import():
    """检查 FastAPI 应用是否可以正常导入"""
    try:
        # 临时添加当前目录到路径
        sys.path.insert(0, '.')
        
        # 尝试导入 main 模块
        import main
        
        # 检查是否有 app 对象
        if hasattr(main, 'app'):
            print("✅ FastAPI 应用导入成功")
            print(f"   应用标题: {main.app.title}")
            print(f"   应用版本: {main.app.version}")
            return True
        else:
            print("❌ main.py 中未找到 'app' 对象")
            return False
            
    except ImportError as e:
        print(f"❌ FastAPI 应用导入失败: {e}")
        return False
    except Exception as e:
        print(f"❌ 应用检查失败: {e}")
        return False

def check_requirements():
    """检查依赖文件内容"""
    requirements_files = [
        'requirements.txt',
        'requirements-pythonanywhere.txt'
    ]
    
    for req_file in requirements_files:
        if Path(req_file).exists():
            print(f"✅ 依赖文件存在: {req_file}")
            try:
                with open(req_file, 'r') as f:
                    content = f.read()
                    if 'fastapi' in content.lower():
                        print("   ✅ 包含 FastAPI 依赖")
                    if 'uvicorn' in content.lower():
                        print("   ✅ 包含 Uvicorn 依赖")
            except Exception as e:
                print(f"   ❌ 读取失败: {e}")

def main():
    """主验证函数"""
    print("=" * 50)
    print("PythonAnywhere FastAPI 部署验证")
    print("=" * 50)
    
    success_count = 0
    total_checks = 0
    
    # 检查必需文件
    files_to_check = [
        ('main.py', 'FastAPI 主文件'),
        ('config.py', '配置文件'),
        ('requirements.txt', '依赖文件'),
        ('start_pythonanywhere.sh', '部署脚本'),
    ]
    
    print("\n📁 文件检查:")
    for filepath, description in files_to_check:
        total_checks += 1
        if check_file_exists(filepath, description):
            success_count += 1
    
    # 检查 Python 语法
    python_files = ['main.py', 'config.py']
    print("\n🐍 Python 语法检查:")
    for filepath in python_files:
        if Path(filepath).exists():
            total_checks += 1
            if check_python_syntax(filepath):
                success_count += 1
    
    # 检查 FastAPI 应用
    print("\n🚀 FastAPI 应用检查:")
    total_checks += 1
    if check_fastapi_import():
        success_count += 1
    
    # 检查依赖
    print("\n📦 依赖文件检查:")
    check_requirements()
    
    # 检查部署脚本权限
    script_path = Path('start_pythonanywhere.sh')
    if script_path.exists():
        print(f"\n🔧 部署脚本权限:")
        import stat
        file_stat = script_path.stat()
        if file_stat.st_mode & stat.S_IEXEC:
            print("✅ 部署脚本有执行权限")
        else:
            print("⚠️  部署脚本需要执行权限，运行: chmod +x start_pythonanywhere.sh")
    
    # 生成启动命令示例
    print(f"\n🎯 启动命令示例:")
    username = os.getenv('USER', 'YOURUSERNAME')
    command = f"/home/{username}/.virtualenvs/leafapi_env/bin/uvicorn --app-dir /home/{username}/leafapi --uds ${{DOMAIN_SOCKET}} main:app"
    print(f"   {command}")
    
    # 总结
    print(f"\n📊 验证结果:")
    print(f"   通过: {success_count}/{total_checks}")
    
    if success_count == total_checks:
        print("\n🎉 所有检查通过！您的项目已准备好部署到 PythonAnywhere")
        print("\n接下来的步骤:")
        print("1. 上传项目文件到 PythonAnywhere")
        print("2. 在 Bash 控制台运行: ./start_pythonanywhere.sh")
        print("3. 或者按照 pythonanywhere_commands.md 手动部署")
        return 0
    else:
        print("\n⚠️  请修复上述问题后再进行部署")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code) 