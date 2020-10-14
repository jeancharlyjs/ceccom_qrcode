FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir /home/qrceccom
WORKDIR /home/qrceccom
COPY requirements.txt /home/qrceccom/
# RUN source .env/bin/activate
RUN pip install -r requirements.txt
RUN pip freeze >> requirements.txt
COPY . /home/qrceccom/
