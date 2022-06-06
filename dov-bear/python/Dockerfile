# For more information, please refer to https://aka.ms/vscode-docker-python
#ARG PORT_ARG=3000
#ARG INSTANCE_NAME_ARG=test
#ARG INSTANCE_HASH_ARG=123
FROM python:3.8-slim

ENV PORT=3000
ENV INSTANCE_NAME=test
ENV INSTANCE_HASH=123
# Install pip requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /app
COPY . /app

EXPOSE ${PORT}


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "main.py"]
