FROM alpine

RUN apk add --update python3 py3-pip

WORKDIR /app

ADD ./app_code /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD python3 dictionary.py

