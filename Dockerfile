FROM python:alpine3.7 

WORKDIR /server

COPY ./ /server/

RUN pip install --upgrade pip

RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow

RUN pip install -r requirements.txt 

EXPOSE 5000

ENTRYPOINT [ "python" ] 

CMD [ "run.py" ] 




