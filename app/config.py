"""
配置管理模块

从 .env 文件中读取配置。

使用方式：
    from app.config import Config
    
    # 方式1：使用显式定义的属性（推荐，简单直接）
    host = Config.HOST
    port = Config.PORT
    debug = Config.DEBUG
    
    # 方式2：使用 get 方法（适用于未显式定义的配置项）
    custom_value = Config.get("CUSTOM_KEY", "default")
    
添加新配置属性：
    在 _init_config_attributes() 函数中添加：
    Config.NEW_KEY = Config.get("NEW_KEY", "default_value")
"""
from pathlib import Path
from typing import Optional
from dotenv import dotenv_values


class Config:
    """配置类，从 .env 文件加载配置"""
    
    _instance: Optional["Config"] = None
    _config: dict[str, str] = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance
    
    def _load_config(self) -> None:
        """从 .env 文件加载配置"""
        # 获取项目根目录
        root_dir = Path(__file__).parent.parent
        
        # 从 .env 文件加载配置
        env_path = root_dir / ".env"
        if env_path.exists():
            env_config = dotenv_values(env_path)
            self._config.update({k: v for k, v in env_config.items() if v is not None})
        else:
            print(f"Warning: .env file not found at {env_path}")
    
    @classmethod
    def get(cls, key: str, default: Optional[str] = None) -> Optional[str]:
        """
        获取配置值
        
        Args:
            key: 配置键名
            default: 默认值，如果配置不存在则返回此值
        
        Returns:
            配置值，如果不存在且未提供默认值则返回 None
        """
        instance = cls()
        return instance._config.get(key, default)
    
    @classmethod
    def get_bool(cls, key: str, default: bool = False) -> bool:
        """
        获取布尔类型配置值
        
        Args:
            key: 配置键名
            default: 默认值
        
        Returns:
            布尔值
        """
        value = cls.get(key)
        if value is None:
            return default
        return value.lower() in ("true", "1", "yes", "on")
    
    @classmethod
    def get_int(cls, key: str, default: Optional[int] = None) -> Optional[int]:
        """
        获取整数类型配置值
        
        Args:
            key: 配置键名
            default: 默认值
        
        Returns:
            整数值，如果转换失败则返回默认值
        """
        value = cls.get(key)
        if value is None:
            return default
        try:
            return int(value)
        except ValueError:
            return default
    
    @classmethod
    def get_float(cls, key: str, default: Optional[float] = None) -> Optional[float]:
        """
        获取浮点数类型配置值
        
        Args:
            key: 配置键名
            default: 默认值
        
        Returns:
            浮点数值，如果转换失败则返回默认值
        """
        value = cls.get(key)
        if value is None:
            return default
        try:
            return float(value)
        except ValueError:
            return default
    
    @classmethod
    def reload(cls) -> None:
        """重新加载配置"""
        cls._instance = None
        cls._config = {}
        cls()
        # 重新初始化类属性
        _init_config_attributes()
    
    def __contains__(self, key: str) -> bool:
        """支持 in 操作符"""
        return key in self._config


# 初始化配置属性
def _init_config_attributes() -> None:
    """初始化 Config 类的属性"""
    # 应用配置
    Config.APP_NAME = Config.get("APP_NAME", "FastAPI Server Template")
    Config.APP_VERSION = Config.get("APP_VERSION", "0.1.0")
    Config.APP_DESCRIPTION = Config.get("APP_DESCRIPTION", "一个简单的 FastAPI 服务器模板")
    
    # 服务器配置
    Config.HOST = Config.get("HOST", "0.0.0.0")
    Config.PORT = Config.get_int("PORT", 8000)
    Config.DEBUG = Config.get_bool("DEBUG", False)
    
    # 日志配置
    Config.LOG_LEVEL = Config.get("LOG_LEVEL", "INFO")
    Config.LOG_FORMAT = Config.get("LOG_FORMAT", "json")
    
    # API 配置
    Config.API_PREFIX = Config.get("API_PREFIX", "/api/v1")
    Config.API_TIMEOUT = Config.get_int("API_TIMEOUT", 30)


# 创建全局配置实例并初始化属性
config = Config()
_init_config_attributes()
