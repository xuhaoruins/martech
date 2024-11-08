# 使用官方 Python 3.10 镜像作为基础镜像
FROM python:3.10-slim-buster

# 设置工作目录为 /app
WORKDIR /app

# 将当前目录的内容复制到容器的 /app 目录中
COPY . /app

# 安装 requirements.txt 中指定的任何需要的包
COPY requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

# 暴露端口 80
EXPOSE 80

ENTRYPOINT ["streamlit", "run", "MarketingWriter.py", "--server.port=80"]