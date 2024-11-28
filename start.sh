#!/bin/bash

# 进入项目目录（替换为你的实际项目路径）
cd /opt/site/beginmama

# 执行数据库迁移
python manage.py migrate --noinput

# 收集静态文件
python manage.py collectstatic --noinput

# 启动 Gunicorn
exec gunicorn Beginmama.wsgi:application \
    --bind 0.0.0.0:8080 \
    --workers 4 \
    --worker-class=gthread \
    --threads 4 \
    --worker-connections=1000 \
    --timeout 300 \
    --keep-alive 65 \
    --max-requests 1000 \
    --max-requests-jitter 50 \
    --backlog 2048 \
    --log-level info \
    --access-logfile /opt/site/beginmama/logs/access.log \
    --error-logfile /opt/site/beginmama/logs/error.log \
    --capture-output \
    --enable-stdio-inheritance