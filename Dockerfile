FROM python:3.10.8-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY src src
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1 
ENTRYPOINT [ "python3", "./src/myapp.py" ]