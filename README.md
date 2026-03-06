## FastAPI Server Template

一个开箱即用的 FastAPI 服务端模板，默认集成：

- `uv` 依赖管理与运行
- `.env` 配置加载（支持 local / production）
- 结构化日志（控制台 + 按天滚动文件）
- 健康检查接口

## 目录结构

- `main/`: 实际服务代码与依赖定义
  - `main/src/app.py`: FastAPI 应用入口
  - `main/src/config.py`: 配置读取（从 `main/.env` 加载）
  - `main/src/logger.py`: 日志配置与 `logger` 实例
  - `main/start.sh`: 启动脚本（选择环境并启动 `uvicorn`）

## 环境要求

- Python `>= 3.11.14`
- 已安装 `uv`

## 快速开始

在项目根目录执行：

```bash
cd main
uv sync
./start.sh --env local
```

默认监听 `0.0.0.0:8080`。

## 环境与配置

启动脚本会根据 `--env` 选择配置文件并复制为 `main/.env`：

- `--env local`：使用 `main/.env.local`（默认加 `--reload`）
- 其他值：使用 `main/.env.production`

### 常用配置项

这些配置由 `main/src/config.py` 读取（可在 `.env.*` 中设置）：

- **应用信息**: `APP_NAME`, `APP_VERSION`, `APP_DESCRIPTION`
- **服务调试**: `DEBUG`
- **日志**: `LOG_LEVEL`, `LOG_PATH`, `LOG_RETENTION_DAYS`
- **API**: `API_PREFIX`（默认 `/api/v1`）

## 接口

- `GET /` 或 `GET /health`：健康检查，返回 `{"status":"ok"}`

## 添加业务路由

在 `main/src/app.py` 的 `business_routers` 列表中追加你的 router，然后服务会自动以 `Config.API_PREFIX` 作为统一前缀挂载。

## 开发辅助

格式化代码：

```bash
cd main
uv run black .
```
