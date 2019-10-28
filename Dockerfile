# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.6.5
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
RUN adduser -D myuser
USER myuser
CMD ["app.py"]