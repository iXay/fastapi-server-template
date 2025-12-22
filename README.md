# FastAPI Server Template

一个简单、易用的 FastAPI 服务器项目模板。

## 特性

- 🚀 基于 FastAPI 构建
- 📦 使用 uv 管理依赖
- 🎯 结构简单，易于理解
- 📖 新手友好，学习路径短

## 快速开始

### 1. 安装 uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 安装依赖

```bash
uv sync
```

### 3. 运行服务器

```bash
uv run uvicorn app.main:app --reload
```

服务器将在 `http://localhost:8000` 启动。

### 4. 访问 API

- 根路径: http://localhost:8000/
- 健康检查: http://localhost:8000/health
- API 文档: http://localhost:8000/docs
- 替代文档: http://localhost:8000/redoc

## 项目结构

```
fastapi-server-template/
├── app/
│   └── main.py          # 主入口文件
├── pyproject.toml       # 项目配置和依赖
└── README.md           # 项目说明
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

