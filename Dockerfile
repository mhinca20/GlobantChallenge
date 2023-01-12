FROM python:3.8-alpine
COPY . /web
WORKDIR /web
RUN apk update && apk add python3-dev \
                        gcc \
                        libc-dev \
                        libffi-dev
RUN pip install -r ./requirements.txt
RUN adduser -D myuser
USER myuser
ENTRYPOINT ["python"]
CMD ["app.py"]