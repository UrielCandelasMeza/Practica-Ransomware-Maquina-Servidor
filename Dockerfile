FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN uv install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uv", "run", "fastapi", "run"]