FROM python:3.10.6
WORKDIR /src
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY ./nbt_technical_task /nbt_technical_task