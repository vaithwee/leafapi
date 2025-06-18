from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# 可选导入uvicorn（仅用于本地开发）
try:
    import uvicorn
except ImportError:
    uvicorn = None

# 创建FastAPI应用实例
app = FastAPI(
    title="LeafAPI",
    description="一个基于FastAPI的后端API项目",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境中应该指定具体的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 数据模型
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    is_active: bool = True

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# 模拟数据存储
items_db = []
next_id = 1

# 根路径
@app.get("/")
async def root():
    return {
        "message": "欢迎使用LeafAPI",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "docs": "/docs"
    }

# 健康检查
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

# 获取所有项目
@app.get("/items", response_model=List[Item])
async def get_items():
    return items_db

# 获取单个项目
@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="项目未找到")

# 创建项目
@app.post("/items", response_model=Item)
async def create_item(item: ItemCreate):
    global next_id
    new_item = {
        "id": next_id,
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "is_active": True
    }
    items_db.append(new_item)
    next_id += 1
    return new_item

# 更新项目
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemCreate):
    for i, existing_item in enumerate(items_db):
        if existing_item["id"] == item_id:
            updated_item = {
                "id": item_id,
                "name": item.name,
                "description": item.description,
                "price": item.price,
                "is_active": existing_item["is_active"]
            }
            items_db[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="项目未找到")

# 删除项目
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for i, item in enumerate(items_db):
        if item["id"] == item_id:
            deleted_item = items_db.pop(i)
            return {"message": f"项目 '{deleted_item['name']}' 已删除"}
    raise HTTPException(status_code=404, detail="项目未找到")

# 本地开发运行
if __name__ == "__main__":
    if uvicorn:
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    else:
        print("警告: uvicorn未安装，无法启动本地开发服务器")
        print("请运行: pip install uvicorn") 