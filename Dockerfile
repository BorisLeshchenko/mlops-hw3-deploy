FROM python:3.11-slim

WORKDIR /app

# устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# копируем код и модель
COPY app ./app

# переменная версии модели по умолчанию
ENV MODEL_VERSION=v1.0.0

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
