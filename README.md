# FastAPI Server Template

一个简单、易用的 FastAPI 服务器项目模板。

## 特性

- 🚀 基于 FastAPI 构建
- 📦 使用 uv 管理依赖
- 🎯 结构简单，易于理解
- 📖 新手友好，学习路径短
- ⚙️ 多环境配置管理，支持公共配置和环境特定配置

## 快速开始

### 1. 安装 uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 安装依赖

```bash
uv sync
```

### 3. 配置环境

复制 `.env.example` 文件为 `.env`，并根据需要修改配置：

```bash
cp .env.example .env
```

然后编辑 `.env` 文件，配置应用所需的参数。配置文件会从 `.env` 文件中读取，环境变量不会覆盖文件配置。

### 4. 运行服务器

```bash
uv run uvicorn app.main:app --reload
```

服务器将在 `http://localhost:8000` 启动。

### 5. 访问 API

- 根路径: http://localhost:8000/
- 健康检查: http://localhost:8000/health
- 配置信息: http://localhost:8000/config
- API 文档: http://localhost:8000/docs
- 替代文档: http://localhost:8000/redoc

## 项目结构

```
fastapi-server-template/
├── app/
│   ├── main.py          # 主入口文件
│   └── config.py        # 配置管理模块
├── .env                 # 配置文件（需要从 .env.example 复制）
├── .env.example         # 配置文件示例
├── pyproject.toml       # 项目配置和依赖
└── README.md           # 项目说明
```

## 配置系统使用

### 基本用法

```python
from app.config import Config

# 方式1：使用显式定义的属性（推荐，简单直接）
host = Config.HOST
port = Config.PORT
debug = Config.DEBUG
app_name = Config.APP_NAME

# 方式2：使用 get 方法（适用于未显式定义的配置项）
custom_value = Config.get("CUSTOM_KEY", "default_value")
custom_int = Config.get_int("CUSTOM_INT", 100)
```

### 添加新的配置属性

如果需要在代码中使用 `Config.XXX` 的方式访问配置，需要在 `app/config.py` 的 `_init_config_attributes()` 函数中显式定义：

```python
def _init_config_attributes() -> None:
    """初始化 Config 类的属性"""
    # 现有配置...
    
    # 添加新配置
    Config.DATABASE_URL = Config.get("DATABASE_URL", "postgresql://localhost/mydb")
    Config.REDIS_HOST = Config.get("REDIS_HOST", "localhost")
    Config.REDIS_PORT = Config.get_int("REDIS_PORT", 6379)
```

### 类型转换方法

```python
# 获取字符串（默认值可选）
value = Config.get("KEY", "default")

# 获取布尔值
debug = Config.get_bool("DEBUG", False)

# 获取整数
port = Config.get_int("PORT", 8000)

# 获取浮点数
timeout = Config.get_float("TIMEOUT", 30.0)
```

### 重新加载配置

```python
# 在运行时重新加载配置（例如配置热更新）
Config.reload()
```

## 开发

### 添加新依赖

```bash
uv add <package-name>
```

### 运行代码格式化

```bash
uv run ruff format .
```

### 运行代码检查

```bash
uv run ruff check .
```

## 许可证

MIT

