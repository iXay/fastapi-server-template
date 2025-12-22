"""
日志管理模块

使用方式：
    from app.logger import logger
    logger.info("这是一条信息日志")
"""
import logging
import logging.handlers
import sys
from pathlib import Path

from app.config import Config


def setup_logger() -> logging.Logger:
    """设置并返回配置好的日志器"""
    logger = logging.getLogger("app")
    logger.setLevel(getattr(logging, Config.LOG_LEVEL.upper(), logging.INFO))
    if logger.handlers:
        return logger
    
    # 日志格式（包含毫秒、函数名、文件名和行数）
    
    fmt = "%(asctime)s.%(msecs)03d [%(levelname)-8s %(name)s:%(filename)s:%(lineno)d:%(funcName)s] %(message)s"
    formatter = logging.Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S")
    
    # 控制台处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # 文件处理器（使用标准库的TimedRotatingFileHandler）
    if Config.LOG_PATH:
        try:
            log_path = Path(Config.LOG_PATH)
            log_path.parent.mkdir(parents=True, exist_ok=True)
            
            # 使用TimedRotatingFileHandler按天轮转，自动清理旧日志
            file_handler = logging.handlers.TimedRotatingFileHandler(
                filename=str(log_path),
                when='midnight',  # 每天午夜轮转
                interval=1,  # 每1天
                backupCount=Config.LOG_RETENTION_DAYS,  # 保留指定天数的日志
                encoding='utf-8'
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except Exception as e:
            logger.warning(f"Failed to setup file handler: {e}")
    
    logger.propagate = False
    return logger


# 创建全局日志器实例
logger = setup_logger()
