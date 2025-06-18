#!/usr/bin/env python3
"""
LeafAPI 启动脚本
提供开发和生产环境的启动选项
"""

import sys
import uvicorn
import argparse
from config import settings

def main():
    parser = argparse.ArgumentParser(description="启动 LeafAPI 服务器")
    parser.add_argument(
        "--env", 
        choices=["dev", "prod"], 
        default="dev",
        help="运行环境 (dev: 开发模式, prod: 生产模式)"
    )
    parser.add_argument(
        "--host", 
        default="0.0.0.0",
        help="绑定主机地址 (默认: 0.0.0.0)"
    )
    parser.add_argument(
        "--port", 
        type=int, 
        default=8000,
        help="端口号 (默认: 8000)"
    )
    parser.add_argument(
        "--workers", 
        type=int, 
        default=1,
        help="工作进程数 (仅生产模式, 默认: 1)"
    )
    
    args = parser.parse_args()
    
    print(f"🚀 启动 {settings.PROJECT_NAME} v{settings.PROJECT_VERSION}")
    print(f"📍 环境: {'开发模式' if args.env == 'dev' else '生产模式'}")
    print(f"🌐 地址: http://{args.host}:{args.port}")
    
    if args.env == "dev":
        print("🔧 开发模式: 启用热重载和调试")
        uvicorn.run(
            "main:app",
            host=args.host,
            port=args.port,
            reload=True,
            log_level="info"
        )
    else:
        print(f"⚡ 生产模式: {args.workers} 个工作进程")
        uvicorn.run(
            "main:app",
            host=args.host,
            port=args.port,
            workers=args.workers,
            log_level="warning"
        )

if __name__ == "__main__":
    main() 