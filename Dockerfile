FROM python:3.7-alpine
ADD ./src/requirements.txt /app/requirements.txt
WORKDIR /app/
RUN pip install -r requirements.txt
ADD ./src/ /app
CMD ["python", "app.py"]
