FROM python:3.13

WORKDIR /university

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["uvicorn" , "main:app" , "--host","0.0.0.0","--port","8080"]