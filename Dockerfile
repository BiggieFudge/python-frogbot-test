# 🔴 Showcase: IaC Scanning
# FrogBot will flag: EOL vulnerable base image (python:3.6), running as root (no USER directive)
FROM python:3.6

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 5000

CMD ["python", "app.py"]
