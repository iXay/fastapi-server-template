"""
FastAPI 服务器主入口
"""
from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Server Template",
    description="一个简单的 FastAPI 服务器模板",
    version="0.1.0",
)


@app.get("/")
async def root():
    """根路径"""
    return {"message": "Hello, FastAPI!"}


@app.get("/health")
async def health():
    """健康检查端点"""
    return {"status": "ok"}

