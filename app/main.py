"""
FastAPI 服务器主入口
"""
from fastapi import FastAPI
from app.config import Config

# 从配置中读取应用信息
app = FastAPI(
    title=Config.APP_NAME,
    description=Config.APP_DESCRIPTION,
    version=Config.APP_VERSION,
    debug=Config.DEBUG,
)


@app.get("/")
async def root():
    """根路径"""
    return {"message": "Hello, FastAPI!"}


@app.get("/health")
async def health():
    """健康检查端点"""
    return {"status": "ok"}


@app.get("/config")
async def get_config():
    """获取配置信息（演示配置系统的使用）"""
    return {
        # 演示属性访问方式
        "app_name": Config.APP_NAME,
        "host": Config.HOST,
        "port": Config.PORT,
        "debug": Config.DEBUG,
        "log_level": Config.LOG_LEVEL,
        "api_prefix": Config.API_PREFIX,
        # 演示 get 方法（适用于未显式定义的配置项）
        "api_timeout": Config.get_int("API_TIMEOUT"),
    }

