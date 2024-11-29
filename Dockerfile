# 使用官方 Python 镜像作为基础镜像

FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 安装系统依赖
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY . .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install gunicorn

# 收集静态文件
RUN python manage.py collectstatic --noinput

# 暴露端口
EXPOSE 8080

# 启动命令
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "Beginmama.wsgi:application"] 