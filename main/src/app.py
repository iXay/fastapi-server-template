"""
Server 主入口
"""

from fastapi import FastAPI

from config import Config
from logger import logger

# 初始化日志
logger.info("Starting Server...")

# 从配置中读取应用信息
app = FastAPI(
    title=Config.APP_NAME,
    description=Config.APP_DESCRIPTION,
    version=Config.APP_VERSION,
    debug=Config.DEBUG,
)

# 按业务挂载路由，统一添加 API 前缀
# 添加新业务时，只需在此列表中添加对应的 router
business_routers = []

for router in business_routers:
    app.include_router(router, prefix=Config.API_PREFIX)


@app.get("/")
@app.get("/health")
async def health():
    """健康检查端点"""
    logger.debug("Health check endpoint accessed")
    return {"status": "ok"}
