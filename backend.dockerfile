FROM python:3.9-alpine

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY spending ./spending
COPY spendingexercise ./spendingexercise
COPY manage.py ./manage.py

RUN python3 manage.py migrate

EXPOSE "8000"

CMD ["python3", "manage.py", "runserver"]