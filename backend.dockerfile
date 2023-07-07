# FROM registry.cn-zhangjiakou.aliyuncs.com/dvadmin-pro/python38-base-backend:latest
FROM python:3.10.12

WORKDIR /backend/

COPY ./backend/requirements.txt /backend/

RUN python3 -m pip install -i  https://mirrors.aliyun.com/pypi/simple/ --upgrade pip
RUN python3 -m pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt; 


COPY ./backend/ /backend/

# RUN chmod +x /backend/start.sh

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" , "--workers", "10", "--proxy-headers", "--forwarded-allow-ips='*'"]