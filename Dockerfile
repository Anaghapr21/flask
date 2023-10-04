FROM python:3.10

WORKDIR /blueprint

COPY requirements.txt .
RUN pip install flask_smorest
RUN pip install -r requirements.txt

COPY . .
CMD ["flask","run","--host","0.0.0.0"]
