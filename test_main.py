from fastapi.testclient import TestClient
from main import app

# 创建测试客户端
client = TestClient(app)

def test_read_main():
    """测试根路径"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "欢迎使用LeafAPI" in data["message"]
    assert data["version"] == "1.0.0"

def test_health_check():
    """测试健康检查端点"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"

def test_get_empty_items():
    """测试获取空项目列表"""
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []

def test_create_item():
    """测试创建项目"""
    item_data = {
        "name": "测试项目",
        "description": "这是一个测试项目",
        "price": 99.99
    }
    response = client.post("/items", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["description"] == item_data["description"]
    assert data["price"] == item_data["price"]
    assert data["id"] == 1
    assert data["is_active"] == True

def test_get_item():
    """测试获取特定项目"""
    # 先创建一个项目
    item_data = {
        "name": "获取测试项目",
        "description": "用于测试获取功能",
        "price": 50.0
    }
    create_response = client.post("/items", json=item_data)
    item_id = create_response.json()["id"]
    
    # 获取项目
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == item_data["name"]

def test_get_nonexistent_item():
    """测试获取不存在的项目"""
    response = client.get("/items/999")
    assert response.status_code == 404

def test_update_item():
    """测试更新项目"""
    # 先创建一个项目
    item_data = {
        "name": "原始项目",
        "description": "原始描述",
        "price": 30.0
    }
    create_response = client.post("/items", json=item_data)
    item_id = create_response.json()["id"]
    
    # 更新项目
    update_data = {
        "name": "更新后的项目",
        "description": "更新后的描述",
        "price": 45.0
    }
    response = client.put(f"/items/{item_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_data["name"]
    assert data["description"] == update_data["description"]
    assert data["price"] == update_data["price"]

def test_delete_item():
    """测试删除项目"""
    # 先创建一个项目
    item_data = {
        "name": "待删除项目",
        "description": "这个项目将被删除",
        "price": 25.0
    }
    create_response = client.post("/items", json=item_data)
    item_id = create_response.json()["id"]
    
    # 删除项目
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert "已删除" in data["message"]
    
    # 验证项目已被删除
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 404 