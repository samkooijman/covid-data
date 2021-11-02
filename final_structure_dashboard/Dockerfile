FROM python:3

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
COPY ./apps /usr/src/app/apps

ENV PORT 8050

EXPOSE $PORT

CMD [ "python", "./index.py" ]