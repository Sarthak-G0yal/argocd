FROM python:3.15.0-slim
WORKDIR /app

COPY requirement.txt /app/

# RUN ["ls", "sync", "--frozen", "--no-install-project"]
RUN pip install -r requirement.txt

COPY . /app
# RUN ["/usr/bin/uv", "sync", "--frozen"]

EXPOSE 8000

CMD ["uvicorn","main:app","--host","0.0.0.0"]
