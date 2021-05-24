FROM python:3

WORKDIR /app

ADD ./app_code /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD python dictionary.py

