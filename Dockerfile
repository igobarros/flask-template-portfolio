FROM python:3.7

COPY . /flask-template-portifolio

WORKDIR /flask-template-portifolio

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["app.py"]