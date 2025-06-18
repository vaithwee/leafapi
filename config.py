import os
from typing import List

class Settings:
    """应用配置类"""
    
    # 基础配置
    PROJECT_NAME: str = "LeafAPI"
    PROJECT_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    
    # 服务器配置
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    
    # CORS配置
    ALLOWED_HOSTS: List[str] = ["*"]
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8080",
        "https://yourdomain.com"  # 替换为你的域名
    ]
    
    # 安全配置
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-super-secret-key-change-in-production")
    
    # 数据库配置（如果需要）
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    
    # PythonAnywhere特定配置
    PYTHONANYWHERE_USERNAME: str = os.getenv("PYTHONANYWHERE_USERNAME", "yourusername")
    
    class Config:
        env_file = ".env"

# 创建设置实例
settings = Settings() 