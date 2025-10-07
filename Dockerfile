FROM python:3.10-slim

WORKDIR /app
COPY . .
RUN apt update && apt install -y ffmpeg && pip install -r requirements.txt

CMD ["python3", "main.py"]
