FROM python:3.9

EXPOSE 10001

WORKDIR /service

COPY . ./

RUN pip install -r dependences.txt

ENTRYPOINT ["uvicorn", "main_api:app", "--port", "10001", "--host", "0.0.0.0"]