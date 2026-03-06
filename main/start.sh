#!/bin/bash
# 启动脚本：设置 PYTHONPATH 并运行服务器

# 获取脚本所在目录（项目根目录）
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 默认环境为 local（开发环境）
ENV="local"

# 解析参数：支持 --env 参数指定环境
UVICORN_ARGS=()
while [[ $# -gt 0 ]]; do
    case $1 in
        --env)
            ENV="$2"
            shift 2
            ;;
        *)
            UVICORN_ARGS+=("$1")
            shift
            ;;
    esac
done

# 根据环境选择对应的 .env 文件
if [ "$ENV" = "local" ]; then
    ENV_FILE=".env.local"
else
    ENV_FILE=".env.production"
fi

# 检查环境文件是否存在
ENV_PATH="${SCRIPT_DIR}/${ENV_FILE}"
if [ ! -f "$ENV_PATH" ]; then
    echo "Error: Environment file not found: $ENV_PATH"
    exit 1
fi

# 将对应的环境文件复制为 .env（供 config.py 读取）
# 先删除旧的 .env 文件（如果存在）
rm -f "${SCRIPT_DIR}/.env"
cp "$ENV_PATH" "${SCRIPT_DIR}/.env"

echo "Starting server with environment: $ENV (using $ENV_FILE)"

# local 环境自动添加 --reload 参数
if [ "$ENV" = "local" ]; then
    UVICORN_ARGS=("--reload" "${UVICORN_ARGS[@]}")
fi

# 切换到项目目录，确保 uv 能找到正确的 pyproject.toml 和 .venv
cd "${SCRIPT_DIR}" || exit 1

# 运行 uvicorn，设置默认 host 和 port，用户传的参数会覆盖默认值
PYTHONPATH=${SCRIPT_DIR}/src uv run uvicorn src.app:app --host 0.0.0.0 --port 8080 "${UVICORN_ARGS[@]}"

