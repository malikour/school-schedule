FROM python:3.9-slim
RUN apt-get update && apt-get install -y git
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR /code
COPY . .
CMD ["python", "main.py"]
